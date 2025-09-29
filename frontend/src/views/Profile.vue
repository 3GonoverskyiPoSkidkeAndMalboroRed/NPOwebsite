<template>
  <div class="min-h-screen bg-background">
    <div class="container mx-auto px-4 py-8">
      <div class="max-w-4xl mx-auto">
        <!-- Заголовок -->
        <div class="mb-8">
          <h1 class="text-3xl font-bold text-foreground mb-2">Личный кабинет</h1>
          <p class="text-muted-foreground">Управление вашими данными и настройками</p>
        </div>

        <!-- Форма входа/регистрации -->
        <div v-if="!isAuthenticated" class="grid md:grid-cols-2 gap-8">
          <!-- Форма входа -->
          <Card class="p-6">
            <CardHeader>
              <CardTitle>Вход в систему</CardTitle>
              <CardDescription>Войдите в свой аккаунт</CardDescription>
            </CardHeader>
            <CardContent>
              <form @submit.prevent="login" class="space-y-4">
                <div>
                  <Label for="login-username">Логин</Label>
                  <Input
                    id="login-username"
                    v-model="loginForm.login"
                    type="text"
                    placeholder="Введите логин"
                    required
                  />
                </div>
                <div>
                  <Label for="login-password">Пароль</Label>
                  <Input
                    id="login-password"
                    v-model="loginForm.password"
                    type="password"
                    placeholder="Введите пароль"
                    required
                  />
                </div>
                <Button type="submit" class="w-full" :disabled="isLoading">
                  <Loader2 v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
                  Войти
                </Button>
              </form>
            </CardContent>
          </Card>

          <!-- Форма регистрации -->
          <Card class="p-6">
            <CardHeader>
              <CardTitle>Регистрация</CardTitle>
              <CardDescription>Создайте новый аккаунт</CardDescription>
            </CardHeader>
            <CardContent>
              <form @submit.prevent="register" class="space-y-4">
                <div>
                  <Label for="reg-login">Логин</Label>
                  <Input
                    id="reg-login"
                    v-model="registerForm.login"
                    type="text"
                    placeholder="Введите логин"
                    required
                  />
                </div>
                <div>
                  <Label for="reg-password">Пароль</Label>
                  <Input
                    id="reg-password"
                    v-model="registerForm.password"
                    type="password"
                    placeholder="Введите пароль"
                    required
                  />
                </div>
                <div>
                  <Label for="reg-organization">Организация</Label>
                  <Input
                    id="reg-organization"
                    v-model="registerForm.organization"
                    type="text"
                    placeholder="Название организации"
                    required
                  />
                </div>
                <div>
                  <Label for="reg-fullname">ФИО</Label>
                  <Input
                    id="reg-fullname"
                    v-model="registerForm.full_name"
                    type="text"
                    placeholder="Фамилия Имя Отчество"
                    required
                  />
                </div>
                <div>
                  <Label for="reg-position">Должность</Label>
                  <Input
                    id="reg-position"
                    v-model="registerForm.position"
                    type="text"
                    placeholder="Должность"
                  />
                </div>
                <div>
                  <Label for="reg-phone">Телефон</Label>
                  <Input
                    id="reg-phone"
                    v-model="registerForm.phone"
                    type="tel"
                    placeholder="+7 (xxx) xxx-xx-xx"
                  />
                </div>
                <div>
                  <Label for="reg-email">Email</Label>
                  <Input
                    id="reg-email"
                    v-model="registerForm.email"
                    type="email"
                    placeholder="email@example.com"
                  />
                </div>
                <Button type="submit" class="w-full" :disabled="isLoading">
                  <Loader2 v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
                  Зарегистрироваться
                </Button>
              </form>
            </CardContent>
          </Card>
        </div>

        <!-- Профиль пользователя -->
        <div v-else class="space-y-6">
          <!-- Навигация по табам -->
          <div class="border-b border-border">
            <nav class="-mb-px flex space-x-8">
              <button
                @click="activeTab = 'profile'"
                :class="[
                  'py-2 px-1 border-b-2 font-medium text-sm transition-colors',
                  activeTab === 'profile'
                    ? 'border-primary text-primary'
                    : 'border-transparent text-muted-foreground hover:text-foreground hover:border-border'
                ]"
              >
                Профиль
              </button>
              <button
                @click="activeTab = 'software-updates'"
                :class="[
                  'py-2 px-1 border-b-2 font-medium text-sm transition-colors',
                  activeTab === 'software-updates'
                    ? 'border-primary text-primary'
                    : 'border-transparent text-muted-foreground hover:text-foreground hover:border-border'
                ]"
              >
                Обновление ПО
              </button>
            </nav>
          </div>

          <!-- Содержимое табов -->
          <div v-if="activeTab === 'profile'" class="space-y-6">
            <!-- Информация о пользователе -->
            <Card class="p-6">
              <CardHeader>
                <CardTitle>Информация о пользователе</CardTitle>
                <CardDescription>Ваши личные данные</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="grid md:grid-cols-2 gap-4">
                  <div>
                    <Label class="text-sm font-medium">Логин</Label>
                    <p class="text-sm text-muted-foreground">{{ userData.login }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Организация</Label>
                    <p class="text-sm text-muted-foreground">{{ userData.organization }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">ФИО</Label>
                    <p class="text-sm text-muted-foreground">{{ userData.full_name }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Должность</Label>
                    <p class="text-sm text-muted-foreground">{{ userData.position || 'Не указано' }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Телефон</Label>
                    <p class="text-sm text-muted-foreground">{{ userData.phone || 'Не указано' }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Email</Label>
                    <p class="text-sm text-muted-foreground">{{ userData.email || 'Не указано' }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Дата регистрации</Label>
                    <p class="text-sm text-muted-foreground">{{ formatDate(userData.created_at) }}</p>
                  </div>
                </div>
              </CardContent>
            </Card>

            <!-- Редактирование профиля -->
            <Card class="p-6">
              <CardHeader>
                <CardTitle>Редактировать профиль</CardTitle>
                <CardDescription>Обновите ваши данные</CardDescription>
              </CardHeader>
              <CardContent>
                <form @submit.prevent="updateProfile" class="space-y-4">
                  <div class="grid md:grid-cols-2 gap-4">
                    <div>
                      <Label for="edit-organization">Организация</Label>
                      <Input
                        id="edit-organization"
                        v-model="editForm.organization"
                        type="text"
                        placeholder="Название организации"
                      />
                    </div>
                    <div>
                      <Label for="edit-fullname">ФИО</Label>
                      <Input
                        id="edit-fullname"
                        v-model="editForm.full_name"
                        type="text"
                        placeholder="Фамилия Имя Отчество"
                      />
                    </div>
                    <div>
                      <Label for="edit-position">Должность</Label>
                      <Input
                        id="edit-position"
                        v-model="editForm.position"
                        type="text"
                        placeholder="Должность"
                      />
                    </div>
                    <div>
                      <Label for="edit-phone">Телефон</Label>
                      <Input
                        id="edit-phone"
                        v-model="editForm.phone"
                        type="tel"
                        placeholder="+7 (xxx) xxx-xx-xx"
                      />
                    </div>
                    <div class="md:col-span-2">
                      <Label for="edit-email">Email</Label>
                      <Input
                        id="edit-email"
                        v-model="editForm.email"
                        type="email"
                        placeholder="email@example.com"
                      />
                    </div>
                  </div>
                  <div class="flex gap-2">
                    <Button type="submit" :disabled="isLoading">
                      <Loader2 v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
                      Сохранить изменения
                    </Button>
                    <Button type="button" variant="destructive" @click="logout">
                      Выйти
                    </Button>
                  </div>
                </form>
              </CardContent>
            </Card>
          </div>

          <!-- Таб "Обновление ПО" -->
          <div v-if="activeTab === 'software-updates'" class="space-y-6">
            <!-- Текущая версия ПО -->
            <Card class="p-6">
              <CardHeader>
                <CardTitle>Текущая версия ПО</CardTitle>
                <CardDescription>Информация о версии программного обеспечения</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="grid md:grid-cols-2 gap-4">
                  <div>
                    <Label class="text-sm font-medium">Версия системы</Label>
                    <p class="text-sm text-muted-foreground">{{ softwareInfo.version }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Дата последнего обновления</Label>
                    <p class="text-sm text-muted-foreground">{{ softwareInfo.lastUpdate }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Статус обновлений</Label>
                    <p class="text-sm text-muted-foreground">
                      <span :class="softwareInfo.updateStatus === 'available' ? 'text-green-600' : 'text-muted-foreground'">
                        {{ softwareInfo.updateStatus === 'available' ? 'Доступны обновления' : 'Система актуальна' }}
                      </span>
                    </p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Автоматические обновления</Label>
                    <p class="text-sm text-muted-foreground">
                      {{ softwareInfo.autoUpdate ? 'Включены' : 'Отключены' }}
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>

            <!-- Доступные обновления -->
            <Card class="p-6" v-if="softwareInfo.updateStatus === 'available'">
              <CardHeader>
                <CardTitle>Доступные обновления</CardTitle>
                <CardDescription>Новые версии программного обеспечения</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="space-y-4">
                  <div class="border rounded-lg p-4">
                    <div class="flex justify-between items-start">
                      <div>
                        <h4 class="font-medium">Версия {{ availableUpdate.version }}</h4>
                        <p class="text-sm text-muted-foreground mt-1">{{ availableUpdate.description }}</p>
                        <p class="text-xs text-muted-foreground mt-2">Размер: {{ availableUpdate.size }}</p>
                      </div>
                      <Button @click="downloadUpdate" :disabled="isDownloading">
                        <Loader2 v-if="isDownloading" class="mr-2 h-4 w-4 animate-spin" />
                        Скачать
                      </Button>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            <!-- Настройки обновлений -->
            <Card class="p-6">
              <CardHeader>
                <CardTitle>Настройки обновлений</CardTitle>
                <CardDescription>Управление автоматическими обновлениями</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="space-y-4">
                  <div class="flex items-center justify-between">
                    <div>
                      <Label class="text-sm font-medium">Автоматические обновления</Label>
                      <p class="text-sm text-muted-foreground">Автоматически загружать и устанавливать обновления</p>
                    </div>
                    <Button
                      @click="toggleAutoUpdate"
                      :variant="softwareInfo.autoUpdate ? 'default' : 'outline'"
                      size="sm"
                    >
                      {{ softwareInfo.autoUpdate ? 'Включено' : 'Отключено' }}
                    </Button>
                  </div>
                  
                  <div class="flex items-center justify-between">
                    <div>
                      <Label class="text-sm font-medium">Проверка обновлений</Label>
                      <p class="text-sm text-muted-foreground">Проверить наличие новых обновлений</p>
                    </div>
                    <Button @click="checkForUpdates" :disabled="isCheckingUpdates" variant="outline" size="sm">
                      <Loader2 v-if="isCheckingUpdates" class="mr-2 h-4 w-4 animate-spin" />
                      Проверить
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>

            <!-- История обновлений -->
            <Card class="p-6">
              <CardHeader>
                <CardTitle>История обновлений</CardTitle>
                <CardDescription>Список установленных обновлений</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="space-y-3">
                  <div v-for="update in updateHistory" :key="update.id" class="flex justify-between items-center py-2 border-b last:border-b-0">
                    <div>
                      <p class="text-sm font-medium">Версия {{ update.version }}</p>
                      <p class="text-xs text-muted-foreground">{{ update.date }}</p>
                    </div>
                    <div class="text-xs text-muted-foreground">
                      {{ update.status }}
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Loader2 } from 'lucide-vue-next'

// Состояние аутентификации
const isAuthenticated = ref(false)
const isLoading = ref(false)
const userData = ref<any>(null)

// Состояние табов
const activeTab = ref('profile')

// Состояние для обновлений ПО
const isDownloading = ref(false)
const isCheckingUpdates = ref(false)

// Информация о ПО
const softwareInfo = ref({
  version: '1.2.3',
  lastUpdate: '15.12.2024',
  updateStatus: 'available', // 'available' | 'up-to-date'
  autoUpdate: true
})

// Доступное обновление
const availableUpdate = ref({
  version: '1.3.0',
  description: 'Новые функции анализа, улучшенная производительность и исправления ошибок',
  size: '45.2 MB'
})

// История обновлений
const updateHistory = ref([
  {
    id: 1,
    version: '1.2.3',
    date: '15.12.2024',
    status: 'Установлено'
  },
  {
    id: 2,
    version: '1.2.1',
    date: '01.12.2024',
    status: 'Установлено'
  },
  {
    id: 3,
    version: '1.2.0',
    date: '20.11.2024',
    status: 'Установлено'
  }
])

// Формы
const loginForm = reactive({
  login: '',
  password: ''
})

const registerForm = reactive({
  login: '',
  password: '',
  organization: '',
  full_name: '',
  position: '',
  phone: '',
  email: ''
})

const editForm = reactive({
  organization: '',
  full_name: '',
  position: '',
  phone: '',
  email: ''
})

// API базовый URL
const API_BASE = 'http://192.168.81.74:8000'

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

// Функция входа
const login = async () => {
  try {
    isLoading.value = true
    const response = await apiRequest('/auth/login', {
      method: 'POST',
      body: JSON.stringify(loginForm)
    })
    
    localStorage.setItem('token', response.access_token)
    await loadUserData()
    isAuthenticated.value = true
  } catch (error) {
    alert('Ошибка входа: ' + error.message)
  } finally {
    isLoading.value = false
  }
}

// Функция регистрации
const register = async () => {
  try {
    isLoading.value = true
    await apiRequest('/auth/register', {
      method: 'POST',
      body: JSON.stringify(registerForm)
    })
    
    alert('Регистрация успешна! Теперь вы можете войти в систему.')
    
    // Очищаем форму регистрации
    Object.assign(registerForm, {
      login: '',
      password: '',
      organization: '',
      full_name: '',
      position: '',
      phone: '',
      email: ''
    })
  } catch (error) {
    alert('Ошибка регистрации: ' + error.message)
  } finally {
    isLoading.value = false
  }
}

// Функция загрузки данных пользователя
const loadUserData = async () => {
  try {
    const data = await apiRequest('/auth/me')
    userData.value = data
    
    // Заполняем форму редактирования
    Object.assign(editForm, {
      organization: data.organization || '',
      full_name: data.full_name || '',
      position: data.position || '',
      phone: data.phone || '',
      email: data.email || ''
    })
  } catch (error) {
    console.error('Ошибка загрузки данных пользователя:', error)
  }
}

// Функция обновления профиля
const updateProfile = async () => {
  try {
    isLoading.value = true
    const data = await apiRequest('/auth/me', {
      method: 'PUT',
      body: JSON.stringify(editForm)
    })
    
    userData.value = data
    alert('Профиль успешно обновлен!')
  } catch (error) {
    alert('Ошибка обновления профиля: ' + error.message)
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

// Функция форматирования даты
const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('ru-RU')
}

// Функции для работы с обновлениями ПО
const downloadUpdate = async () => {
  try {
    isDownloading.value = true
    // Здесь будет логика загрузки обновления
    await new Promise(resolve => setTimeout(resolve, 2000)) // Имитация загрузки
    alert('Обновление успешно загружено!')
  } catch (error) {
    alert('Ошибка загрузки обновления: ' + error.message)
  } finally {
    isDownloading.value = false
  }
}

const toggleAutoUpdate = () => {
  softwareInfo.value.autoUpdate = !softwareInfo.value.autoUpdate
  alert(`Автоматические обновления ${softwareInfo.value.autoUpdate ? 'включены' : 'отключены'}`)
}

const checkForUpdates = async () => {
  try {
    isCheckingUpdates.value = true
    // Здесь будет логика проверки обновлений
    await new Promise(resolve => setTimeout(resolve, 1500)) // Имитация проверки
    
    // Имитация результата проверки
    const hasUpdates = Math.random() > 0.5
    if (hasUpdates) {
      softwareInfo.value.updateStatus = 'available'
      alert('Доступны новые обновления!')
    } else {
      softwareInfo.value.updateStatus = 'up-to-date'
      alert('Система актуальна, обновления не найдены.')
    }
  } catch (error) {
    alert('Ошибка проверки обновлений: ' + error.message)
  } finally {
    isCheckingUpdates.value = false
  }
}

// Проверяем аутентификацию при загрузке
onMounted(async () => {
  const token = localStorage.getItem('token')
  if (token) {
    try {
      await loadUserData()
      isAuthenticated.value = true
    } catch (error) {
      localStorage.removeItem('token')
    }
  }
})
</script>
