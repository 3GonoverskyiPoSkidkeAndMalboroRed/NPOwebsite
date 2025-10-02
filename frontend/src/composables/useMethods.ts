import { ref, computed, readonly } from 'vue'

export interface MethodDocumentation {
  title: string
  description: string
  link?: string
}

export interface MethodEquipment {
  name: string
  description: string
  specifications?: string
}

export interface Method {
  id: number
  title: string
  standards_description?: string
  method_description?: string
  description_content?: string[]
  limitations?: string
  procedure?: string[]
  documentation?: MethodDocumentation[]
  equipment?: MethodEquipment[]
  category: string
  is_active: number
  created_at: string
  updated_at: string
}

export interface MethodItem {
  title: string
  image: string
  link: string
  items: {
    text: string
    image: string
    link: string
  }[]
}

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export function useMethods() {
  const methods = ref<Method[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  // Получить все методики
  const fetchMethods = async (category?: string) => {
    loading.value = true
    error.value = null
    
    try {
      const url = category 
        ? `${API_BASE_URL}/methods?category=${category}&is_active=1`
        : `${API_BASE_URL}/methods?is_active=1`
      
      const response = await fetch(url)
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      methods.value = data
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Ошибка загрузки методик'
      console.error('Ошибка загрузки методик:', err)
    } finally {
      loading.value = false
    }
  }

  // Получить методику по ID
  const fetchMethodById = async (id: number): Promise<Method | null> => {
    loading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${API_BASE_URL}/methods/${id}`)
      
      if (!response.ok) {
        if (response.status === 404) {
          return null
        }
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      return data
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Ошибка загрузки методики'
      console.error('Ошибка загрузки методики:', err)
      return null
    } finally {
      loading.value = false
    }
  }

  // Получить категории методик
  const fetchCategories = async (): Promise<string[]> => {
    try {
      const response = await fetch(`${API_BASE_URL}/methods/categories/list`)
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      return data
    } catch (err) {
      console.error('Ошибка загрузки категорий:', err)
      return []
    }
  }

  // Группировка методик по категориям для отображения
  const groupedMethods = computed(() => {
    const groups: { [key: string]: Method[] } = {}
    
    methods.value.forEach(method => {
      if (!groups[method.category]) {
        groups[method.category] = []
      }
      groups[method.category].push(method)
    })
    
    return groups
  })

  // Преобразование данных для компонента MethodBlock
  const methodBlocks = computed((): MethodItem[] => {
    const blocks: MethodItem[] = []
    
    Object.entries(groupedMethods.value).forEach(([category, categoryMethods]) => {
      const categoryInfo = getCategoryInfo(category)
      
      blocks.push({
        title: categoryInfo.title,
        image: categoryInfo.image,
        link: categoryInfo.link,
        items: categoryMethods.map(method => ({
          text: method.title,
          image: "/10.png",
          link: `/methods/${method.id}`,
          id: method.id
        }))
      })
    })
    
    return blocks
  })

  // Информация о категориях
  const getCategoryInfo = (category: string) => {
    const categoryMap: { [key: string]: { title: string; image: string; link: string } } = {
      'oil': {
        title: "Методики анализа нефти и нефтепродуктов",
        image: "/лого-методик/Газ овая промышленность/Определение общей серы в природном и углеводородных газах.png",
        link: "/methods-oil"
      },
      'eco': {
        title: "Методики анализа в области экологии",
        image: "/home-photo/ecologylittle.png",
        link: "/methods-eco"
      },
      'mining': {
        title: "Методики анализа в горнорудной промышленности",
        image: "/home-photo/gornlittle.png",
        link: "/methods-mining"
      },
      'metallurgy': {
        title: "Методики анализа в продукции металлургии",
        image: "/home-photo/metlittle.png",
        link: "/methods-metallurgy"
      },
      'diagnostics': {
        title: "Методики анализа для диагностики и контроля",
        image: "/home-photo/diagnostikalittle2.png",
        link: "/methods-diagnostics"
      },
      'gas': {
        title: "Методики анализа в газовой промышленности",
        image: "/home-photo/06bba93af58b01ffc5367e30d6485f7c.png",
        link: "/methods-gas"
      }
    }
    
    return categoryMap[category] || {
      title: `Методики категории ${category}`,
      image: "/10.png",
      link: "/methods"
    }
  }

  return {
    methods,
    loading,
    error,
    groupedMethods,
    methodBlocks,
    fetchMethods,
    fetchMethodById,
    fetchCategories
  }
}
