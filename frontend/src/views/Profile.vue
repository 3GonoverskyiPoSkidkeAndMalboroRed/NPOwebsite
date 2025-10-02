<template>
  <div class="min-h-screen bg-background">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 py-4 sm:py-6 lg:py-8">
      <div class="max-w-4xl mx-auto">
        <!-- Заголовок -->
        <div class="mb-6 sm:mb-8">
          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-foreground mb-2">Личный кабинет</h1>
          <p class="text-sm sm:text-base text-muted-foreground">Управление вашими данными и настройками</p>
        </div>

        <!-- Профиль пользователя -->
        <div class="space-y-6">
          <!-- Навигация по табам -->
          <div class="border-b border-border">
            <nav class="-mb-px flex flex-wrap space-x-2 sm:space-x-8">
              <button
                @click="activeTab = 'auth'"
                :class="[
                  'py-2 px-1 border-b-2 font-medium text-xs sm:text-sm transition-colors whitespace-nowrap',
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
                  'py-2 px-1 border-b-2 font-medium text-xs sm:text-sm transition-colors whitespace-nowrap',
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
                  'py-2 px-1 border-b-2 font-medium text-xs sm:text-sm transition-colors whitespace-nowrap',
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
          <div v-if="activeTab === 'auth'" class="space-y-4 sm:space-y-6">
            <Card class="p-4 sm:p-6">
              <CardHeader class="pb-4">
                <CardTitle class="text-lg sm:text-xl">Вход в систему</CardTitle>
                <CardDescription class="text-sm sm:text-base">Войдите в свой аккаунт для доступа к профилю и обновлениям ПО</CardDescription>
              </CardHeader>
              <CardContent>
                <form @submit.prevent="handleLogin" class="space-y-4">
                  <div>
                    <Label for="login-serial" class="text-sm sm:text-base">Серийный номер прибора</Label>
                    <Input
                      id="login-serial"
                      v-model="loginForm.serial_number"
                      type="text"
                      placeholder="SE0260001, G6001, MSW8037 и т.д."
                      class="mt-1"
                      required
                    />
                  </div>
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <Label for="login-inn" class="text-sm sm:text-base">ИНН</Label>
                      <Input
                        id="login-inn"
                        v-model="loginForm.inn"
                        type="text"
                        placeholder="ИНН организации"
                        class="mt-1"
                        required
                      />
                    </div>
                    <div>
                      <Label for="login-kpp" class="text-sm sm:text-base">КПП</Label>
                      <Input
                        id="login-kpp"
                        v-model="loginForm.kpp"
                        type="text"
                        placeholder="КПП организации"
                        class="mt-1"
                        required
                      />
                    </div>
                  </div>
                  <div>
                    <Label for="login-password" class="text-sm sm:text-base">Пароль</Label>
                    <Input
                      id="login-password"
                      v-model="loginForm.password"
                      type="password"
                      placeholder="Введите пароль"
                      class="mt-1"
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

            <Card class="p-4 sm:p-6">
              <CardHeader class="pb-4">
                <CardTitle class="text-lg sm:text-xl">Регистрация</CardTitle>
                <CardDescription class="text-sm sm:text-base">Создайте новый аккаунт</CardDescription>
              </CardHeader>
              <CardContent>
                <form @submit.prevent="handleRegister" class="space-y-4">
                  <div>
                    <Label for="reg-serial" class="text-sm sm:text-base">Серийный номер прибора</Label>
                    <Input
                      id="reg-serial"
                      v-model="registerForm.serial_number"
                      type="text"
                      placeholder="SE0260001, G6001, MSW8037 и т.д."
                      class="mt-1"
                      required
                    />
                    <p class="text-xs text-muted-foreground mt-1">
                      Примеры: SE02 60000-60999, G 6000-6999, MSW 8037,8040,12000-12999
                    </p>
                  </div>
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <Label for="reg-inn" class="text-sm sm:text-base">ИНН</Label>
                      <Input
                        id="reg-inn"
                        v-model="registerForm.inn"
                        type="text"
                        placeholder="ИНН организации"
                        class="mt-1"
                        required
                      />
                    </div>
                    <div>
                      <Label for="reg-kpp" class="text-sm sm:text-base">КПП</Label>
                      <Input
                        id="reg-kpp"
                        v-model="registerForm.kpp"
                        type="text"
                        placeholder="КПП организации"
                        class="mt-1"
                        required
                      />
                    </div>
                  </div>
                  <div>
                    <Label for="reg-password" class="text-sm sm:text-base">Пароль</Label>
                    <Input
                      id="reg-password"
                      v-model="registerForm.password"
                      type="password"
                      placeholder="Введите пароль"
                      class="mt-1"
                      required
                    />
                  </div>
                  <div>
                    <Label for="reg-fullname" class="text-sm sm:text-base">ФИО</Label>
                    <Input
                      id="reg-fullname"
                      v-model="registerForm.full_name"
                      type="text"
                      placeholder="Фамилия Имя Отчество"
                      class="mt-1"
                      @input="handleFullNameInput"
                      required
                    />
                    <p class="text-xs text-muted-foreground mt-1">
                      Введите ФИО на русском языке
                    </p>
                  </div>
                  <div>
                    <Label for="reg-position" class="text-sm sm:text-base">Должность</Label>
                    <Input
                      id="reg-position"
                      v-model="registerForm.position"
                      type="text"
                      placeholder="Должность"
                      class="mt-1"
                      required
                    />
                  </div>
                  <div>
                    <Label for="reg-organization" class="text-sm sm:text-base">Организация</Label>
                    <Input
                      id="reg-organization"
                      v-model="registerForm.organization"
                      type="text"
                      placeholder="Название организации"
                      class="mt-1"
                      required
                    />
                  </div>
                  <div>
                    <Label for="reg-phone" class="text-sm sm:text-base">Телефон</Label>
                    <Input
                      id="reg-phone"
                      v-model="registerForm.phone"
                      type="tel"
                      placeholder="+7 (xxx) xxx-xx-xx"
                      class="mt-1"
                      @input="handlePhoneInput"
                      @paste="handlePhonePaste"
                      required
                    />
                    <p class="text-xs text-muted-foreground mt-1">
                      Введите номер в формате +7 (xxx) xxx-xx-xx
                    </p>
                  </div>
                  <div>
                    <Label for="reg-email" class="text-sm sm:text-base">Email</Label>
                    <Input
                      id="reg-email"
                      v-model="registerForm.email"
                      type="email"
                      placeholder="email@example.com"
                      class="mt-1"
                      required
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

          <div v-if="activeTab === 'profile'" class="space-y-4 sm:space-y-6">
            <!-- Информация о пользователе -->
            <Card class="p-4 sm:p-6">
              <CardHeader class="pb-4">
                <CardTitle class="text-lg sm:text-xl">Информация о пользователе</CardTitle>
                <CardDescription class="text-sm sm:text-base">Ваши личные данные</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <Label class="text-sm font-medium">Серийный номер прибора</Label>
                    <p class="text-sm text-muted-foreground mt-1">{{ userData.serial_number }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">ИНН</Label>
                    <p class="text-sm text-muted-foreground mt-1">{{ userData.inn }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">КПП</Label>
                    <p class="text-sm text-muted-foreground mt-1">{{ userData.kpp }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Организация</Label>
                    <p class="text-sm text-muted-foreground mt-1">{{ userData.organization }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">ФИО</Label>
                    <p class="text-sm text-muted-foreground mt-1">{{ userData.full_name }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Должность</Label>
                    <p class="text-sm text-muted-foreground mt-1">{{ userData.position }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Телефон</Label>
                    <p class="text-sm text-muted-foreground mt-1">{{ userData.phone }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Email</Label>
                    <p class="text-sm text-muted-foreground mt-1">{{ userData.email }}</p>
                  </div>
                  <div>
                    <Label class="text-sm font-medium">Дата регистрации</Label>
                    <p class="text-sm text-muted-foreground mt-1">{{ formatDate(userData.created_at) }}</p>
                  </div>
                </div>
              </CardContent>
            </Card>

            <!-- Редактирование профиля -->
            <Card class="p-4 sm:p-6">
              <CardHeader class="pb-4">
                <CardTitle class="text-lg sm:text-xl">Редактировать профиль</CardTitle>
                <CardDescription class="text-sm sm:text-base">Обновите ваши данные</CardDescription>
              </CardHeader>
              <CardContent>
                <form @submit.prevent="handleUpdateProfile" class="space-y-4">
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <Label for="edit-organization" class="text-sm sm:text-base">Организация</Label>
                      <Input
                        id="edit-organization"
                        v-model="editForm.organization"
                        type="text"
                        placeholder="Название организации"
                        class="mt-1"
                      />
                    </div>
                    <div>
                      <Label for="edit-fullname" class="text-sm sm:text-base">ФИО</Label>
                      <Input
                        id="edit-fullname"
                        v-model="editForm.full_name"
                        type="text"
                        placeholder="Фамилия Имя Отчество"
                        class="mt-1"
                        @input="handleFullNameInput"
                      />
                    </div>
                    <div>
                      <Label for="edit-position" class="text-sm sm:text-base">Должность</Label>
                      <Input
                        id="edit-position"
                        v-model="editForm.position"
                        type="text"
                        placeholder="Должность"
                        class="mt-1"
                      />
                    </div>
                    <div>
                      <Label for="edit-phone" class="text-sm sm:text-base">Телефон</Label>
                      <Input
                        id="edit-phone"
                        v-model="editForm.phone"
                        type="tel"
                        placeholder="+7 (xxx) xxx-xx-xx"
                        class="mt-1"
                        @input="handlePhoneInput"
                        @paste="handlePhonePaste"
                      />
                    </div>
                    <div class="sm:col-span-2">
                      <Label for="edit-email" class="text-sm sm:text-base">Email</Label>
                      <Input
                        id="edit-email"
                        v-model="editForm.email"
                        type="email"
                        placeholder="email@example.com"
                        class="mt-1"
                      />
                    </div>
                  </div>
                  <div class="flex flex-col sm:flex-row gap-2">
                    <Button type="submit" :disabled="isLoading" class="w-full sm:w-auto">
                      <Loader2 v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
                      Сохранить изменения
                    </Button>
                    <Button type="button" variant="destructive" @click="handleLogout" class="w-full sm:w-auto">
                      Выйти
                    </Button>
                  </div>
                </form>
              </CardContent>
            </Card>
          </div>

          <!-- Таб "Обновление ПО" -->
          <div v-if="activeTab === 'software-updates'" class="space-y-4 sm:space-y-6">
            <!-- Загрузка файлов обновления -->
            <Card class="p-4 sm:p-6">
              <CardHeader class="pb-4">
                <CardTitle class="text-lg sm:text-xl">Загрузка файлов обновления</CardTitle>
                <CardDescription class="text-sm sm:text-base">Загрузите новые файлы обновления ПО</CardDescription>
              </CardHeader>
              <CardContent>
                <form @submit.prevent="uploadUpdate" class="space-y-4">
                  <div>
                    <Label for="upload-file" class="text-sm sm:text-base">Файл обновления</Label>
                    <Input
                      id="upload-file"
                      type="file"
                      @change="handleFileSelect"
                      accept=".zip,.exe,.msi,.deb,.rpm,.dmg,.pkg"
                      class="mt-1"
                      required
                    />
                    <p class="text-xs text-muted-foreground mt-1">
                      Поддерживаемые форматы: ZIP, EXE, MSI, DEB, RPM, DMG, PKG
                    </p>
                  </div>
                  <div>
                    <Label for="upload-version" class="text-sm sm:text-base">Версия</Label>
                    <Input
                      id="upload-version"
                      v-model="uploadForm.version"
                      type="text"
                      placeholder="Например: 1.3.0"
                      class="mt-1"
                      required
                    />
                  </div>
                  <div>
                    <Label for="upload-description" class="text-sm sm:text-base">Описание</Label>
                    <Textarea
                      id="upload-description"
                      v-model="uploadForm.description"
                      placeholder="Описание изменений в новой версии"
                      rows="3"
                      class="mt-1"
                    />
                  </div>
                  <Button type="submit" :disabled="isUploading" class="w-full sm:w-auto">
                    <Loader2 v-if="isUploading" class="mr-2 h-4 w-4 animate-spin" />
                    Загрузить файл
                  </Button>
                </form>
              </CardContent>
            </Card>

            <!-- Доступные обновления -->
            <Card class="p-4 sm:p-6">
              <CardHeader class="pb-4">
                <CardTitle class="text-lg sm:text-xl">Доступные обновления</CardTitle>
                <CardDescription class="text-sm sm:text-base">
                  Новые версии программного обеспечения 
                  <span v-if="availableUpdates.length > 0">(найдено: {{ availableUpdates.length }})</span>
                  <span v-else class="text-muted-foreground">(обновления не найдены)</span>
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div v-if="availableUpdates.length === 0" class="text-center text-muted-foreground py-6 sm:py-8">
                  <p class="text-sm sm:text-base">Доступные обновления не найдены</p>
                  <p class="text-xs sm:text-sm mt-2">Загрузите файлы обновления, используя форму выше</p>
                </div>
                <div v-else class="space-y-4">
                  <div v-for="update in availableUpdates" :key="update.id" class="border rounded-lg p-3 sm:p-4">
                    <div class="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-3">
                      <div class="flex-1">
                        <h4 class="font-medium text-sm sm:text-base">Версия {{ update.version }}</h4>
                        <p class="text-xs sm:text-sm text-muted-foreground mt-1">{{ update.description || 'Описание не указано' }}</p>
                        <p class="text-xs text-muted-foreground mt-2">
                          Размер: {{ update.file_size ? update.file_size.toFixed(1) + ' МБ' : 'Неизвестно' }}
                        </p>
                        <p class="text-xs text-muted-foreground">
                          Загружено: {{ formatDate(update.created_at) }}
                        </p>
                      </div>
                      <div class="flex flex-col sm:flex-row gap-2">
                        <Button @click="downloadUpdate(update.id)" :disabled="isDownloading" size="sm" class="w-full sm:w-auto">
                          <Loader2 v-if="isDownloading" class="mr-2 h-4 w-4 animate-spin" />
                          Скачать
                        </Button>
                        <Button 
                          @click="deleteUpdate(update.id)" 
                          variant="destructive" 
                          size="sm"
                          class="w-full sm:w-auto"
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
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import { Loader2 } from 'lucide-vue-next'
import { useAuth } from '@/composables/useAuth'
import { useInputMasks } from '@/composables/useInputMasks'

// Используем composable для авторизации
const { isAuthenticated, userData, isLoading, login, register, logout, updateProfile, checkAuth } = useAuth()

// Используем composable для масок ввода
const { 
  handleFullNameInput, 
  handlePhoneInput, 
  handlePhonePaste
} = useInputMasks()

// Состояние табов - по умолчанию показываем авторизацию
const activeTab = ref('auth')

// Состояние для обновлений ПО
const isDownloading = ref(false)
const isUploading = ref(false)

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
  serial_number: '',
  inn: '',
  kpp: '',
  password: ''
})

const registerForm = reactive({
  serial_number: '',
  inn: '',
  kpp: '',
  password: '',
  full_name: '',
  position: '',
  organization: '',
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
    if (!token) {
      throw new Error('Токен авторизации не найден')
    }

    const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/software-updates/upload`, {
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

    await response.json()
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
    if (!token) {
      throw new Error('Токен авторизации не найден')
    }

    const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/software-updates/${updateId}/download`, {
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
    if (!token) {
      throw new Error('Токен авторизации не найден')
    }

    const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/software-updates/${updateId}`, {
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
    if (!token) {
      console.log('Токен не найден, пропускаем загрузку обновлений')
      return
    }

    const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/software-updates`, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    })

    if (!response.ok) {
      throw new Error(`Ошибка загрузки списка обновлений: ${response.status}`)
    }

    const updates = await response.json()
    availableUpdates.value = updates
    updateHistory.value = updates
    console.log('Загружены обновления ПО:', updates)
  } catch (error: any) {
    console.error('Ошибка загрузки списка обновлений:', error)
    // Очищаем списки при ошибке
    availableUpdates.value = []
    updateHistory.value = []
  }
}


// Watcher для отслеживания изменений активного таба
watch(activeTab, async (newTab) => {
  // Если пользователь пытается перейти к защищенным разделам без авторизации
  if (!isAuthenticated.value && (newTab === 'profile' || newTab === 'software-updates')) {
    // Сбрасываем таб на форму авторизации
    activeTab.value = 'auth'
  }
  
  // Если переключаемся на вкладку обновлений ПО и пользователь авторизован
  if (newTab === 'software-updates' && isAuthenticated.value) {
    await loadSoftwareUpdates()
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
