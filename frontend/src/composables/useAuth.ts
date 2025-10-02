import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

// Глобальное состояние авторизации
const isAuthenticated = ref(false)
const userData = ref<any>(null)
const isLoading = ref(false)

// API базовый URL
const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export function useAuth() {
  const router = useRouter()

  // Функции для работы с API
  const apiRequest = async (url: string, options: RequestInit = {}) => {
    const token = localStorage.getItem('token')
    const headers = {
      'Content-Type': 'application/json',
      ...(token && { 'Authorization': `Bearer ${token}` }),
      ...options.headers
    }

    const response = await fetch(`${API_BASE}${url}`, {
      ...options,
      headers
    })

    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.detail || 'Ошибка запроса')
    }

    return response.json()
  }

  // Функция загрузки данных пользователя
  const loadUserData = async () => {
    try {
      const data = await apiRequest('/auth/me')
      userData.value = data
      return data
    } catch (error: any) {
      console.error('Ошибка загрузки данных пользователя:', error)
      throw error
    }
  }

  // Функция входа
  const login = async (loginForm: { 
    serial_number: string; 
    inn: string; 
    kpp: string; 
    password: string 
  }) => {
    try {
      isLoading.value = true
      const response = await apiRequest('/auth/login', {
        method: 'POST',
        body: JSON.stringify(loginForm)
      })
      
      localStorage.setItem('token', response.access_token)
      await loadUserData()
      isAuthenticated.value = true
      return response
    } catch (error: any) {
      throw error
    } finally {
      isLoading.value = false
    }
  }

  // Функция регистрации
  const register = async (registerForm: any) => {
    try {
      isLoading.value = true
      await apiRequest('/auth/register', {
        method: 'POST',
        body: JSON.stringify(registerForm)
      })
    } catch (error: any) {
      throw error
    } finally {
      isLoading.value = false
    }
  }

  // Функция выхода
  const logout = () => {
    localStorage.removeItem('token')
    isAuthenticated.value = false
    userData.value = null
  }

  // Функция обновления профиля
  const updateProfile = async (editForm: any) => {
    try {
      isLoading.value = true
      const data = await apiRequest('/auth/me', {
        method: 'PUT',
        body: JSON.stringify(editForm)
      })
      
      userData.value = data
      return data
    } catch (error: any) {
      throw error
    } finally {
      isLoading.value = false
    }
  }

  // Функция проверки авторизации при загрузке
  const checkAuth = async () => {
    const token = localStorage.getItem('token')
    if (token) {
      try {
        await loadUserData()
        isAuthenticated.value = true
        return true
      } catch (error: any) {
        // Если токен недействителен, удаляем его
        localStorage.removeItem('token')
        isAuthenticated.value = false
        userData.value = null
        return false
      }
    } else {
      isAuthenticated.value = false
      userData.value = null
      return false
    }
  }

  // Guard для защищенных маршрутов
  const requireAuth = () => {
    if (!isAuthenticated.value) {
      router.push('/profile')
      return false
    }
    return true
  }

  return {
    // Состояние
    isAuthenticated: computed(() => isAuthenticated.value),
    userData: computed(() => userData.value),
    isLoading: computed(() => isLoading.value),
    
    // Методы
    login,
    register,
    logout,
    updateProfile,
    loadUserData,
    checkAuth,
    requireAuth
  }
}
