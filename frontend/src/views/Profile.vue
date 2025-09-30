<template>
  <div class="min-h-screen bg-background">
    <div class="container mx-auto px-4 py-8">
      <div class="max-w-4xl mx-auto">
        <!-- Заголовок -->
        <div class="mb-8">
          <h1 class="text-3xl font-bold text-foreground mb-2">Личный кабинет</h1>
          <p class="text-muted-foreground">Управление вашими данными и настройками</p>
        </div>

        <!-- Профиль пользователя -->
        <div class="space-y-6">
          <!-- Навигация по табам -->
          <div class="border-b border-border">
            <nav class="-mb-px flex space-x-8">
              <button
                @click="activeTab = 'auth'"
                :class="[
                  'py-2 px-1 border-b-2 font-medium text-sm transition-colors',
                  activeTab === 'auth'
                    ? 'border-primary text-primary'
                    : 'border-transparent text-muted-foreground hover:text-foreground hover:border-border'
                ]"
              >
                Авторизация
              </button>
              <button
                v-if="isAuthenticated"
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
                v-if="isAuthenticated"
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
          <!-- Таб авторизации -->
          <div v-if="activeTab === 'auth'" class="space-y-6">
            <Card class="p-6">
              <CardHeader>
                <CardTitle>Вход в систему</CardTitle>
                <CardDescription>Войдите в свой аккаунт для доступа к профилю и обновлениям ПО</CardDescription>
              </CardHeader>
              <CardContent>
                <form @submit.prevent="handleLogin" class="space-y-4">
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

            <Card class="p-6">
              <CardHeader>
                <CardTitle>Регистрация</CardTitle>
                <CardDescription>Создайте новый аккаунт</CardDescription>
              </CardHeader>
              <CardContent>
                <form @submit.prevent="handleRegister" class="space-y-4">
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
                <form @submit.prevent="handleUpdateProfile" class="space-y-4">
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
                    <Button type="button" variant="destructive" @click="handleLogout">
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
            <!-- <Card class="p-6">
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
            </Card> -->

            <!-- Загрузка файлов обновления -->
            <Card class="p-6">
              <CardHeader>
                <CardTitle>Загрузка файлов обновления</CardTitle>
                <CardDescription>Загрузите новые файлы обновления ПО</CardDescription>
              </CardHeader>
              <CardContent>
                <form @submit.prevent="uploadUpdate" class="space-y-4">
                  <div>
                    <Label for="upload-file">Файл обновления</Label>
                    <Input
                      id="upload-file"
                      type="file"
                      @change="handleFileSelect"
                      accept=".zip,.exe,.msi,.deb,.rpm,.dmg,.pkg"
                      required
                    />
                    <p class="text-xs text-muted-foreground mt-1">
                      Поддерживаемые форматы: ZIP, EXE, MSI, DEB, RPM, DMG, PKG
                    </p>
                  </div>
                  <div>
                    <Label for="upload-version">Версия</Label>
                    <Input
                      id="upload-version"
                      v-model="uploadForm.version"
                      type="text"
                      placeholder="Например: 1.3.0"
                      required
                    />
                  </div>
                  <div>
                    <Label for="upload-description">Описание</Label>
                    <Textarea
                      id="upload-description"
                      v-model="uploadForm.description"
                      placeholder="Описание изменений в новой версии"
                      rows="3"
                    />
                  </div>
                  <Button type="submit" :disabled="isUploading">
                    <Loader2 v-if="isUploading" class="mr-2 h-4 w-4 animate-spin" />
                    Загрузить файл
                  </Button>
                </form>
              </CardContent>
            </Card>

            <!-- Доступные обновления -->
            <Card class="p-6" v-if="availableUpdates.length > 0">
              <CardHeader>
                <CardTitle>Доступные обновления</CardTitle>
                <CardDescription>Новые версии программного обеспечения</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="space-y-4">
                  <div v-for="update in availableUpdates" :key="update.id" class="border rounded-lg p-4">
                    <div class="flex justify-between items-start">
                      <div>
                        <h4 class="font-medium">Версия {{ update.version }}</h4>
                        <p class="text-sm text-muted-foreground mt-1">{{ update.description || 'Описание не указано' }}</p>
                        <p class="text-xs text-muted-foreground mt-2">
                          Размер: {{ update.file_size ? update.file_size.toFixed(1) + ' МБ' : 'Неизвестно' }}
                        </p>
                        <p class="text-xs text-muted-foreground">
                          Загружено: {{ formatDate(update.created_at) }}
                        </p>
                      </div>
                      <div class="flex gap-2">
                        <Button @click="downloadUpdate(update.id)" :disabled="isDownloading" size="sm">
                          <Loader2 v-if="isDownloading" class="mr-2 h-4 w-4 animate-spin" />
                          Скачать
                        </Button>
                        <Button 
                          @click="deleteUpdate(update.id)" 
                          variant="destructive" 
                          size="sm"
                          v-if="update.uploaded_by === userData?.id"
                        >
                          Удалить
                        </Button>
                      </div>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            <!-- Настройки обновлений -->
            <!-- <Card class="p-6">
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
            </Card> -->

            <!-- История обновлений -->
            <!-- <Card class="p-6">
              <CardHeader>
                <CardTitle>История обновлений</CardTitle>
                <CardDescription>Список загруженных файлов обновления</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="space-y-3" v-if="updateHistory.length > 0">
                  <div v-for="update in updateHistory" :key="update.id" class="flex justify-between items-center py-2 border-b last:border-b-0">
                    <div>
                      <p class="text-sm font-medium">Версия {{ update.version }}</p>
                      <p class="text-xs text-muted-foreground">{{ formatDate(update.created_at) }}</p>
                      <p class="text-xs text-muted-foreground">{{ update.file_name }}</p>
                    </div>
                    <div class="text-xs text-muted-foreground">
                      {{ update.file_size ? update.file_size.toFixed(1) + ' МБ' : 'Неизвестно' }}
                    </div>
                  </div>
                </div>
                <div v-else class="text-center text-muted-foreground py-4">
                  <p>История обновлений пуста</p>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  </div> -->

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import { Loader2 } from 'lucide-vue-next'
import { useAuth } from '@/composables/useAuth'

// Роутер для перенаправления
const router = useRouter()

// Используем composable для авторизации
const { isAuthenticated, userData, isLoading, login, register, logout, updateProfile, loadUserData, checkAuth } = useAuth()

// Состояние табов - по умолчанию показываем авторизацию
const activeTab = ref('auth')

// Состояние для обновлений ПО
const isDownloading = ref(false)
const isCheckingUpdates = ref(false)
const isUploading = ref(false)

// Информация о ПО
const softwareInfo = ref({
  version: '1.2.3',
  lastUpdate: '15.12.2024',
  updateStatus: 'up-to-date', // 'available' | 'up-to-date'
  autoUpdate: true
})

// Доступные обновления
const availableUpdates = ref<any[]>([])
const updateHistory = ref<any[]>([])

// Форма загрузки файла
const uploadForm = reactive({
  file: null as File | null,
  version: '',
  description: ''
})

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

// Функция входа
const handleLogin = async () => {
  try {
    await login(loginForm)
    // Переключаемся на таб профиля после успешного входа
    activeTab.value = 'profile'
    // Заполняем форму редактирования
    Object.assign(editForm, {
      organization: userData.value.organization || '',
      full_name: userData.value.full_name || '',
      position: userData.value.position || '',
      phone: userData.value.phone || '',
      email: userData.value.email || ''
    })
  } catch (error: any) {
    alert('Ошибка входа: ' + error.message)
  }
}

// Функция регистрации
const handleRegister = async () => {
  try {
    await register(registerForm)
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
  } catch (error: any) {
    alert('Ошибка регистрации: ' + error.message)
  }
}

// Функция обновления профиля
const handleUpdateProfile = async () => {
  try {
    await updateProfile(editForm)
    alert('Профиль успешно обновлен!')
  } catch (error: any) {
    alert('Ошибка обновления профиля: ' + error.message)
  }
}

// Функция выхода
const handleLogout = () => {
  logout()
  // Переключаемся на таб авторизации после выхода
  activeTab.value = 'auth'
}

// Функция форматирования даты
const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('ru-RU')
}

// Функции для работы с обновлениями ПО
const handleFileSelect = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target.files && target.files[0]) {
    uploadForm.file = target.files[0]
  }
}

const uploadUpdate = async () => {
  if (!uploadForm.file || !uploadForm.version) {
    alert('Пожалуйста, выберите файл и укажите версию')
    return
  }

  try {
    isUploading.value = true
    
    const formData = new FormData()
    formData.append('file', uploadForm.file)
    formData.append('version', uploadForm.version)
    if (uploadForm.description) {
      formData.append('description', uploadForm.description)
    }

    const token = localStorage.getItem('token')
    const response = await fetch(`http://192.168.81.74:8000/software-updates/upload`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`
      },
      body: formData
    })

    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.detail || 'Ошибка загрузки файла')
    }

    const result = await response.json()
    alert('Файл успешно загружен!')
    
    // Очищаем форму
    uploadForm.file = null
    uploadForm.version = ''
    uploadForm.description = ''
    
    // Обновляем списки
    await loadSoftwareUpdates()
    
  } catch (error: any) {
    alert('Ошибка загрузки файла: ' + error.message)
  } finally {
    isUploading.value = false
  }
}

const downloadUpdate = async (updateId: number) => {
  try {
    isDownloading.value = true
    
    const token = localStorage.getItem('token')
    const response = await fetch(`http://192.168.81.74:8000/software-updates/${updateId}/download`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })

    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.detail || 'Ошибка скачивания файла')
    }

    // Создаем ссылку для скачивания
    const blob = await response.blob()
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = response.headers.get('content-disposition')?.split('filename=')[1] || 'update.zip'
    document.body.appendChild(a)
    a.click()
    window.URL.revokeObjectURL(url)
    document.body.removeChild(a)
    
  } catch (error: any) {
    alert('Ошибка скачивания файла: ' + error.message)
  } finally {
    isDownloading.value = false
  }
}

const deleteUpdate = async (updateId: number) => {
  if (!confirm('Вы уверены, что хотите удалить этот файл обновления?')) {
    return
  }

  try {
    const token = localStorage.getItem('token')
    const response = await fetch(`http://192.168.81.74:8000/software-updates/${updateId}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })

    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.detail || 'Ошибка удаления файла')
    }

    alert('Файл успешно удален!')
    await loadSoftwareUpdates()
    
  } catch (error: any) {
    alert('Ошибка удаления файла: ' + error.message)
  }
}

const loadSoftwareUpdates = async () => {
  try {
    const token = localStorage.getItem('token')
    const response = await fetch(`http://192.168.81.74:8000/software-updates`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })

    if (!response.ok) {
      throw new Error('Ошибка загрузки списка обновлений')
    }

    const updates = await response.json()
    availableUpdates.value = updates
    updateHistory.value = updates
  } catch (error: any) {
    console.error('Ошибка загрузки списка обновлений:', error)
  }
}

const toggleAutoUpdate = () => {
  softwareInfo.value.autoUpdate = !softwareInfo.value.autoUpdate
  alert(`Автоматические обновления ${softwareInfo.value.autoUpdate ? 'включены' : 'отключены'}`)
}

const checkForUpdates = async () => {
  try {
    isCheckingUpdates.value = true
    await loadSoftwareUpdates()
    
    if (availableUpdates.value.length > 0) {
      softwareInfo.value.updateStatus = 'available'
      alert('Доступны новые обновления!')
    } else {
      softwareInfo.value.updateStatus = 'up-to-date'
      alert('Система актуальна, обновления не найдены.')
    }
  } catch (error: any) {
    alert('Ошибка проверки обновлений: ' + error.message)
  } finally {
    isCheckingUpdates.value = false
  }
}

// Watcher для отслеживания изменений активного таба
watch(activeTab, (newTab) => {
  // Если пользователь пытается перейти к защищенным разделам без авторизации
  if (!isAuthenticated.value && (newTab === 'profile' || newTab === 'software-updates')) {
    // Сбрасываем таб на форму авторизации
    activeTab.value = 'auth'
  }
})

// Проверяем аутентификацию при загрузке
onMounted(async () => {
  const isAuth = await checkAuth()
  if (isAuth) {
    // Загружаем обновления ПО если пользователь авторизован
    await loadSoftwareUpdates()
    // Переключаемся на таб профиля для авторизованных пользователей
    activeTab.value = 'profile'
    // Заполняем форму редактирования
    Object.assign(editForm, {
      organization: userData.value.organization || '',
      full_name: userData.value.full_name || '',
      position: userData.value.position || '',
      phone: userData.value.phone || '',
      email: userData.value.email || ''
    })
  } else {
    // Если пользователь не авторизован, показываем только вкладку авторизации
    activeTab.value = 'auth'
  }
})
</script>
