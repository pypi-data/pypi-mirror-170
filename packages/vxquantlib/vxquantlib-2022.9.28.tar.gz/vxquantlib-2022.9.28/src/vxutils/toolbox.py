"""api工具箱"""

import importlib
import pathlib
from typing import Any, Union, Dict

import vxutils

try:
    import simplejson as json
except ImportError:
    import json
__all__ = ["import_tools", "vxToolBox"]


def import_tools(mod_path, params=None):
    """导入工具"""

    if mod_path.find(".") > -1:
        class_name = mod_path.split(".")[-1]
        mod_name = ".".join(mod_path.split(".")[:-1])
        mod = importlib.import_module(mod_name)
        tool_cls = getattr(mod, class_name)
    else:
        tool_cls = importlib.import_module(mod_path)

    return tool_cls(**params) if params else tool_cls


@vxutils.singleton
class vxToolBox:
    """api box"""

    def __init__(self, settings: Union[str, Dict] = None) -> None:
        if settings:
            self.loads(settings)

    def __getitem__(self, key: str):
        return self.__dict__[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.__dict__[key] = value

    def __str__(self):
        message = {
            name: (
                f"module {tool.__name__} at id ({id(tool)})"
                if hasattr(tool, "__name__")
                else f"class {tool.__class__.__name__} at id ({id(tool)})"
            )
            for name, tool in self.__dict__.items()
        }

        return f"< {self.__class__.__name__} (id-{id(self)}) : {vxutils.to_json(message)} >"

    def _load_tool(self, tool_name: str, tool_params: dict, settings: dict) -> None:
        """加载当个工具"""
        if "class" not in tool_params:
            vxutils.logger.warning(f"{tool_name}导入参数格式错误，请修改后，重新导入.")
            return

        if "params" not in tool_params:
            self.__dict__[tool_name] = import_tools(tool_params["class"])
            vxutils.logger.info(f"工具{tool_name} 加载成功.")
            return

        kwargs = {}
        for k, v in tool_params["params"].items():
            if v in settings and v not in self.__dict__:
                self._load_tool(v, settings[v], settings)
            kwargs[k] = self.__dict__.get(v, v)

        self.__dict__[tool_name] = import_tools(tool_params["class"], kwargs)
        vxutils.logger.info(f"工具{tool_name} 加载成功.")

    def loads(self, settings: dict) -> None:
        """加载工具"""

        if isinstance(settings, str):
            settings = pathlib.Path(settings)
            if not settings.exists() or not settings.is_file():
                vxutils.logger.error(f"{settings} 文件不存在.", exc_info=True)
                return

            with open(settings.as_posix(), "r", encoding="utf-8") as f:
                settings = json.load(f)

        for tool_name, tool_params in settings.items():
            if tool_name in self.__dict__:
                vxutils.logger.warning(f"工具名称:{tool_name}已加载，无需重复加载")
                continue

            try:
                self._load_tool(tool_name, tool_params, settings)
            except Exception as err:
                vxutils.logger.error(
                    f"加载工具{tool_params['class']}({tool_params.get('params','')}) 初始化失败: {err}",
                    exc_info=True,
                )
