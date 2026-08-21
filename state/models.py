from dataclasses import dataclass,field
@dataclass
class BrandState:
 evidence:list=field(default_factory=list); human_approval:bool=False
