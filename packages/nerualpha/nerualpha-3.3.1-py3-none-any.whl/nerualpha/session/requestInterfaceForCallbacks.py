from dataclasses import dataclass, field
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod

from nerualpha.session.IPayloadWithCallback import IPayloadWithCallback
from nerualpha.session.IActionPayload import IActionPayload
from nerualpha.session.ISession import ISession
from nerualpha.request.requestMethods import RequestMethods

@dataclass
class RequestInterfaceForCallbacks:
    method: str
    action: IActionPayload[IPayloadWithCallback]
    session: ISession
    def __init__(self,session,action,method = RequestMethods.POST):
        self.session = session
        self.action = action
        self.method = method
    
    async def execute(self):
        await self.session.executeAction(self.action,self.method)
        return self.action.payload.callback.id
    
    def reprJSON(self):
        dict = {}
        keywordsMap = {"from_":"from","del_":"del","import_":"import","type_":"type"}
        for key in self.__dict__:
            val = self.__dict__[key]

            if type(val) is list:
                parsedList = []
                for i in val:
                    if hasattr(i,'reprJSON'):
                        parsedList.append(i.reprJSON())
                    else:
                        parsedList.append(i)
                val = parsedList

            if hasattr(val,'reprJSON'):
                val = val.reprJSON()
            if key in keywordsMap:
                key = keywordsMap[key]
            dict.__setitem__(key.replace('_hyphen_', '-'), val)
        return dict
