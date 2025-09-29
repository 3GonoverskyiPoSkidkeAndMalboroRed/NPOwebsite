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
