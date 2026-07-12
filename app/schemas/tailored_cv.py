from pydantic import BaseModel, Field
from typing import List


class WorkExperience(BaseModel):
    company: str = Field(description="Name of the company")
    role: str = Field(description="Job title/role optimized for target job context")
    duration: str = Field(description="Dates of employment, e.g., Jan 2024 - Present")
    bullet_points: List[str] = Field(
        description="3-5 tailored, high-impact bullet points focusing on metrics and relevant stack keywords."
    )


class Education(BaseModel):
    institution: str
    degree: str
    duration: str


class TailoredCV(BaseModel):
    full_name: str
    email: str
    phone: str
    links: List[str] = Field(description="GitHub, LinkedIn, portfolio links")
    professional_summary: str = Field(
        description="A highly strategic, 3-4 sentence professional summary tailored to the target job description."
    )
    skills: List[str] = Field(
        description="Categorized or listed technical keywords matching the job requirements."
    )
    experience: List[WorkExperience]
    education: List[Education]


class FinalTailoredOutput(BaseModel):
    cv: TailoredCV
    cover_letter: str = Field(
        description="A beautifully persuasive, single-page professional cover letter addressing the hiring requirements."
    )
