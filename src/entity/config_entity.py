from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir: Path
    source_data_path: str
    local_data_path: Path
    movies_list_bin: Path
    important_feature: str
    important_feature1: str
    important_feature2: str
    important_feature3: str
    new_feature: str


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    source_data_path: str
    vector_similarity_path: Path


@dataclass(frozen=True)
class RecommendationConfig:
    movies_list_path: str
    vector_similarity_path: Path
    movie_id_url: str
    poster_url: str
