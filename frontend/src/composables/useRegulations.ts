import { ref, computed } from 'vue'
import type { 
  Regulation, 
  RegulationCreate, 
  RegulationUpdate, 
  RegulationFilters, 
  RegulationStats 
} from '@/types/regulations'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

// Состояние
const regulations = ref<Regulation[]>([])
const categories = ref<string[]>([])
const stats = ref<RegulationStats>({ total: 0, categories: 0, modern: 0 })
const loading = ref(false)
const error = ref<string | null>(null)

// Фильтры
const filters = ref<RegulationFilters>({
  category: 'all',
  search: '',
  is_active: 1
})

// Computed свойства
const filteredRegulations = computed(() => {
  let filtered = regulations.value

  // Фильтр по категории
  if (filters.value.category && filters.value.category !== 'all') {
    filtered = filtered.filter(r => r.category === filters.value.category)
  }

  // Поиск по тексту
  if (filters.value.search) {
    const query = filters.value.search.toLowerCase()
    filtered = filtered.filter(r => 
      r.code.toLowerCase().includes(query) ||
      r.title.toLowerCase().includes(query) ||
      r.category.toLowerCase().includes(query)
    )
  }

  return filtered
})

const sortedRegulations = computed(() => {
  return [...filteredRegulations.value].sort((a, b) => {
    if (a.year === 'ISO') return 1
    if (b.year === 'ISO') return -1
    return parseInt(b.year) - parseInt(a.year)
  })
})

// API функции
const fetchRegulations = async (customFilters?: RegulationFilters) => {
  loading.value = true
  error.value = null
  
  try {
    const params = new URLSearchParams()
    const currentFilters = customFilters || filters.value
    
    if (currentFilters.category && currentFilters.category !== 'all') {
      params.append('category', currentFilters.category)
    }
    if (currentFilters.search) {
      params.append('search', currentFilters.search)
    }
    if (currentFilters.is_active !== undefined) {
      params.append('is_active', currentFilters.is_active.toString())
    }

    const response = await fetch(`${API_BASE_URL}/regulations/?${params}`)
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data = await response.json()
    regulations.value = data
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Ошибка загрузки данных'
    console.error('Ошибка загрузки нормативных документов:', err)
  } finally {
    loading.value = false
  }
}

const fetchCategories = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/regulations/categories/list`)
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data = await response.json()
    categories.value = data
  } catch (err) {
    console.error('Ошибка загрузки категорий:', err)
  }
}

const fetchStats = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/regulations/stats/summary`)
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data = await response.json()
    stats.value = data
  } catch (err) {
    console.error('Ошибка загрузки статистики:', err)
  }
}

const fetchRegulationById = async (id: number): Promise<Regulation | null> => {
  try {
    const response = await fetch(`${API_BASE_URL}/regulations/${id}`)
    
    if (!response.ok) {
      if (response.status === 404) {
        return null
      }
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    return await response.json()
  } catch (err) {
    console.error('Ошибка загрузки документа:', err)
    return null
  }
}

const createRegulation = async (regulation: RegulationCreate): Promise<Regulation | null> => {
  try {
    const response = await fetch(`${API_BASE_URL}/regulations/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(regulation)
    })
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data = await response.json()
    regulations.value.push(data)
    return data
  } catch (err) {
    console.error('Ошибка создания документа:', err)
    return null
  }
}

const updateRegulation = async (id: number, regulation: RegulationUpdate): Promise<Regulation | null> => {
  try {
    const response = await fetch(`${API_BASE_URL}/regulations/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(regulation)
    })
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data = await response.json()
    const index = regulations.value.findIndex(r => r.id === id)
    if (index !== -1) {
      regulations.value[index] = data
    }
    return data
  } catch (err) {
    console.error('Ошибка обновления документа:', err)
    return null
  }
}

const deleteRegulation = async (id: number): Promise<boolean> => {
  try {
    const response = await fetch(`${API_BASE_URL}/regulations/${id}`, {
      method: 'DELETE'
    })
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    regulations.value = regulations.value.filter(r => r.id !== id)
    return true
  } catch (err) {
    console.error('Ошибка удаления документа:', err)
    return false
  }
}

// Функции для работы с фильтрами
const setCategory = (category: string) => {
  filters.value.category = category
}

const setSearch = (search: string) => {
  filters.value.search = search
}

const resetFilters = () => {
  filters.value = {
    category: 'all',
    search: '',
    is_active: 1
  }
}

// Инициализация данных
const initializeData = async () => {
  await Promise.all([
    fetchRegulations(),
    fetchCategories(),
    fetchStats()
  ])
}

export function useRegulations() {
  return {
    // Состояние
    regulations: computed(() => regulations.value),
    categories: computed(() => categories.value),
    stats: computed(() => stats.value),
    loading: computed(() => loading.value),
    error: computed(() => error.value),
    
    // Фильтры
    filters: computed(() => filters.value),
    filteredRegulations,
    sortedRegulations,
    
    // API функции
    fetchRegulations,
    fetchCategories,
    fetchStats,
    fetchRegulationById,
    createRegulation,
    updateRegulation,
    deleteRegulation,
    
    // Функции фильтров
    setCategory,
    setSearch,
    resetFilters,
    
    // Инициализация
    initializeData
  }
}
