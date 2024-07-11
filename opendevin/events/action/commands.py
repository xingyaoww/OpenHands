from dataclasses import dataclass
from typing import ClassVar

from opendevin.core.schema import ActionType

from .action import Action, ActionConfirmationStatus, ActionSecurityRisk


@dataclass
class CmdRunAction(Action):
    command: str
    thought: str = ''
    action: str = ActionType.RUN
    runnable: ClassVar[bool] = True
    is_confirmed: ActionConfirmationStatus = ActionConfirmationStatus.CONFIRMED
    security_risk: ActionSecurityRisk = ActionSecurityRisk.UNKNOWN

    @property
    def message(self) -> str:
        return f'Running command: {self.command}'

    def __str__(self) -> str:
        ret = f'**CmdRunAction (source={self.source})**\n'
        if self.thought:
            ret += f'THOUGHT: {self.thought}\n'
        ret += f'COMMAND:\n{self.command}'
        return ret


@dataclass
class CmdKillAction(Action):
    command_id: int
    thought: str = ''
    action: str = ActionType.KILL
    runnable: ClassVar[bool] = True
    is_confirmed: ActionConfirmationStatus = ActionConfirmationStatus.CONFIRMED
    security_risk: ActionSecurityRisk = ActionSecurityRisk.UNKNOWN

    @property
    def message(self) -> str:
        return f'Killing command: {self.command_id}'

    def __str__(self) -> str:
        return f'**CmdKillAction**\n{self.command_id}'


@dataclass
class IPythonRunCellAction(Action):
    code: str
    thought: str = ''
    action: str = ActionType.RUN_IPYTHON
    runnable: ClassVar[bool] = True
    is_confirmed: ActionConfirmationStatus = ActionConfirmationStatus.CONFIRMED
    kernel_init_code: str = ''  # code to run in the kernel (if the kernel is restarted)
    security_risk: ActionSecurityRisk = ActionSecurityRisk.UNKNOWN

    def __str__(self) -> str:
        ret = '**IPythonRunCellAction**\n'
        if self.thought:
            ret += f'THOUGHT: {self.thought}\n'
        ret += f'CODE:\n{self.code}'
        return ret

    @property
    def message(self) -> str:
        return f'Running Python code interactively: {self.code}'
