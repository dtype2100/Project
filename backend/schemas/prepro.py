from pydantic import BaseModel

class PreprocessingJob(BaseModel):
    dag_id: str
    schedule_interval: str
    start_date: str
    script_path: str
    task_id: str

