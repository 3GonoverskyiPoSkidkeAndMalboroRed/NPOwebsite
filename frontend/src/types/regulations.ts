export interface Regulation {
  id: number
  code: string
  title: string
  company: string
  category: string
  year: string
  description?: string
  file_path?: string
  is_active: number
  created_at?: string
  updated_at?: string
}

export interface RegulationCreate {
  code: string
  title: string
  company: string
  category: string
  year: string
  description?: string
  file_path?: string
}

export interface RegulationUpdate {
  code?: string
  title?: string
  company?: string
  category?: string
  year?: string
  description?: string
  file_path?: string
  is_active?: number
}

export interface RegulationFilters {
  category?: string
  search?: string
  is_active?: number
}

export interface RegulationStats {
  total: number
  categories: number
  modern: number
}

export interface RegulationResponse {
  regulations: Regulation[]
  stats: RegulationStats
  categories: string[]
}
