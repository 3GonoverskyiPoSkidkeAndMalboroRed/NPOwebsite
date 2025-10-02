<script setup lang="ts">
import { ref } from 'vue'

// Состояние формы
const formData = ref({
  organization: '',
  fullName: '',
  email: '',
  phone: '',
  model: '',
  serialNumber: '',
  reason: '',
  agreeToProcessing: false
})

const isSubmitting = ref(false)
const isSubmitted = ref(false)

// Обработка отправки формы
const handleSubmit = async (e: Event) => {
  e.preventDefault()
  isSubmitting.value = true
  
  // Имитация отправки формы
  await new Promise(resolve => setTimeout(resolve, 1000))
  
  isSubmitting.value = false
  isSubmitted.value = true
}

// Сброс формы
const resetForm = () => {
  formData.value = {
    organization: '',
    fullName: '',
    email: '',
    phone: '',
    model: '',
    serialNumber: '',
    reason: '',
    agreeToProcessing: false
  }
  isSubmitted.value = false
}
</script>

<template>
  <div class="min-h-screen bg-background">
    <!-- Заголовок страницы -->
    <div class="bg-primary/5 py-16 sm:py-20">
      <div class="container px-4 sm:px-6 lg:px-8">
        <div class="max-w-4xl mx-auto text-center">
          <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold mb-4">
            Обучение и методическая поддержка
          </h1>
          <p class="text-lg sm:text-xl text-muted-foreground max-w-2xl mx-auto">
            Полный аналитический комплекс с методической поддержкой для решения ваших задач
          </p>
        </div>
      </div>
    </div>

    <!-- Основной контент -->
    <div class="container px-4 sm:px-6 lg:px-8 py-16">
      <div class="max-w-4xl mx-auto">
        
        <!-- Введение -->
        <div class="prose prose-sm sm:prose-base lg:prose-lg max-w-none mb-12">
          <div class="bg-muted/50 p-6 rounded-lg">
            <p class="text-lg font-medium mb-4">
              Принцип работы НПО «СПЕКТРОН» - предоставить нашим клиентам не просто прибор, а аналитический комплекс, подготовленный и укомплектованный для решения конкретных аналитических задач.
            </p>
            <p class="text-lg font-medium">
              Поскольку задачи бывают самые различные и часто достаточно сложные, для их реализации требуется серьёзная методическая поддержка.
            </p>
          </div>
        </div>

        <!-- Методическая лаборатория -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Методическая лаборатория</h2>
          
          <div class="bg-primary/10 p-6 rounded-lg mb-8">
            <div class="flex items-start mb-4">
              <div class="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mr-4 flex-shrink-0">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-semibold mb-2">Квалифицированные специалисты</h3>
                <p class="text-sm text-muted-foreground">
                  НПО «СПЕКТРОН» располагает методической лабораторией, укомплектованной квалифицированными методистами и химиками, которые решают весь комплекс вопросов, связанных с проведением анализов конкретных продуктов наших клиентов.
                </p>
              </div>
            </div>
          </div>
          
          <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-4">Наши услуги</h3>
              <ul class="space-y-3">
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Разработка и аттестация методик</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Разработка методических рекомендаций</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Создание градуировок для анализа проб заказчиков</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Разработка рекомендаций по пробоподготовке</span>
                </li>
              </ul>
            </div>
            
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-4">Типовые задачи</h3>
              <p class="text-sm mb-4">
                Для решения многих типовых задач, например, таких, как анализ почвы или определение металлов в нефти и нефтепродуктах, в НПО «СПЕКТРОН» разработан целый ряд методик измерения.
              </p>
              <div class="space-y-2">
                <div class="flex items-center text-sm">
                  <span class="text-primary mr-2">✓</span>
                  <span>Анализ почвы</span>
                </div>
                <div class="flex items-center text-sm">
                  <span class="text-primary mr-2">✓</span>
                  <span>Определение металлов в нефти</span>
                </div>
                <div class="flex items-center text-sm">
                  <span class="text-primary mr-2">✓</span>
                  <span>Анализ нефтепродуктов</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Консультации и поддержка -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Консультации и поддержка</h2>
          
          <div class="bg-primary/10 p-6 rounded-lg mb-8">
            <p class="text-center mb-6">
              Специалисты методического отдела осуществляют консультации и методическую поддержку клиентов на протяжении всего срока эксплуатации наших приборов.
            </p>
            
            <div class="grid md:grid-cols-3 gap-4">
              <div class="bg-background p-4 rounded-lg text-center">
                <div class="w-10 h-10 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-3">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                </div>
                <p class="font-medium mb-1">Телефон</p>
                <p class="text-sm text-muted-foreground">Прямые консультации</p>
              </div>
              
              <div class="bg-background p-4 rounded-lg text-center">
                <div class="w-10 h-10 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-3">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                </div>
                <p class="font-medium mb-1">Электронная почта</p>
                <p class="text-sm text-muted-foreground">Детальные ответы</p>
              </div>
              
              <div class="bg-background p-4 rounded-lg text-center">
                <div class="w-10 h-10 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-3">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                </div>
                <p class="font-medium mb-1">Факс</p>
                <p class="text-sm text-muted-foreground">Документооборот</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Технический минимум -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Технический минимум</h2>
          
          <div class="grid md:grid-cols-2 gap-8">
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-4">Обучение персонала</h3>
              <p class="text-sm mb-4">
                Наши приборы и анализаторы просты в эксплуатации, но тем не менее желательно овладеть навыками работы с программным обеспечением и подготовки проб.
              </p>
              <p class="text-sm">
                НПО «СПЕКТРОН» проводит технический минимум для персонала заказчиков по работе с нашим оборудованием на протяжении всего срока эксплуатации спектрометров и анализаторов.
              </p>
            </div>
            
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-4">Условия обучения</h3>
              <ul class="space-y-3">
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">✓</span>
                  <span class="text-sm">Технический минимум проводится бесплатно</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">✓</span>
                  <span class="text-sm">Обучение на территории нашего предприятия в Санкт-Петербурге</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">✓</span>
                  <span class="text-sm">Заказчик оплачивает только проезд и проживание</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">✓</span>
                  <span class="text-sm">Обучение доступно на протяжении всего срока эксплуатации</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Исследование проб -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Исследование проб</h2>
          
          <div class="bg-muted/50 p-6 rounded-lg">
            <div class="text-center mb-6">
              <div class="w-16 h-16 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
                </svg>
              </div>
              <h3 class="text-xl font-semibold mb-4">Бесплатное исследование проб</h3>
              <p class="text-lg">
                Если наши потенциальные клиенты сомневаются в применимости нашего оборудования для решения своих задач, то мы рекомендуем после консультации со специалистами лаборатории методик отправить нам свои пробы для исследования.
              </p>
              <p class="text-lg font-medium text-primary mt-4">
                Работа с пробами потенциальных заказчиков проводится бесплатно.
              </p>
            </div>
          </div>
        </div>

        <!-- Контактная информация -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Свяжитесь с нами</h2>
          
          <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-4">Контактная информация</h3>
              <div class="space-y-4">
                <div class="flex items-center">
                  <svg class="w-5 h-5 text-primary mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                  <div>
                    <p class="font-medium">Email</p>
                    <a href="mailto:service@spectronxray.ru" class="text-primary hover:underline">
                      service@spectronxray.ru
                    </a>
                  </div>
                </div>
                
                <div class="flex items-center">
                  <svg class="w-5 h-5 text-primary mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  <div>
                    <p class="font-medium">Факс</p>
                    <p class="text-muted-foreground">(812) 325-85-03</p>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-4">Оставить заявку</h3>
              <p class="text-sm mb-4">
                Отправить заявку вы можете по e-mail или факсу, либо заполнить форму ниже.
              </p>
              <div class="space-y-2">
                <div class="flex items-center text-sm">
                  <span class="text-primary mr-2">•</span>
                  <span>Быстрый ответ в течение 24 часов</span>
                </div>
                <div class="flex items-center text-sm">
                  <span class="text-primary mr-2">•</span>
                  <span>Консультации специалистов</span>
                </div>
                <div class="flex items-center text-sm">
                  <span class="text-primary mr-2">•</span>
                  <span>Методическая поддержка</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Форма заявки -->
        <div class="bg-muted/50 p-6 rounded-lg">
          <h2 class="text-2xl font-bold mb-8 text-center">Форма заявки</h2>
          
          <form @submit="handleSubmit" v-if="!isSubmitted">
            <div class="grid md:grid-cols-2 gap-6 mb-6">
              <div>
                <label for="organization" class="block text-sm font-medium mb-2">Название организации *</label>
                <input
                  id="organization"
                  v-model="formData.organization"
                  type="text"
                  required
                  class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="Название вашей организации"
                />
              </div>
              
              <div>
                <label for="fullName" class="block text-sm font-medium mb-2">Ф.И.О. *</label>
                <input
                  id="fullName"
                  v-model="formData.fullName"
                  type="text"
                  required
                  class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="Ваше полное имя"
                />
              </div>
              
              <div>
                <label for="email" class="block text-sm font-medium mb-2">E-mail *</label>
                <input
                  id="email"
                  v-model="formData.email"
                  type="email"
                  required
                  class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="your@email.com"
                />
              </div>
              
              <div>
                <label for="phone" class="block text-sm font-medium mb-2">Контактный телефон *</label>
                <input
                  id="phone"
                  v-model="formData.phone"
                  type="tel"
                  required
                  class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="+7 (xxx) xxx-xx-xx"
                />
              </div>
              
              <div>
                <label for="model" class="block text-sm font-medium mb-2">Модель прибора *</label>
                <input
                  id="model"
                  v-model="formData.model"
                  type="text"
                  required
                  class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="Например: СПЕКТРОСКАН МСВ"
                />
              </div>
              
              <div>
                <label for="serialNumber" class="block text-sm font-medium mb-2">Заводской номер *</label>
                <input
                  id="serialNumber"
                  v-model="formData.serialNumber"
                  type="text"
                  required
                  class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="Заводской номер прибора"
                />
              </div>
            </div>
            
            <div class="mb-6">
              <label for="reason" class="block text-sm font-medium mb-2">Причина обращения *</label>
              <textarea
                id="reason"
                v-model="formData.reason"
                required
                rows="4"
                class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                placeholder="Опишите причину обращения за методической поддержкой..."
              ></textarea>
            </div>
            
            <div class="mb-6">
              <label class="flex items-start">
                <input
                  v-model="formData.agreeToProcessing"
                  type="checkbox"
                  required
                  class="mt-1 mr-3"
                />
                <span class="text-sm">
                  Согласен на обработку персональных данных. *
                </span>
              </label>
            </div>
            
            <div class="text-center">
              <button
                type="submit"
                :disabled="isSubmitting"
                class="px-8 py-3 bg-primary text-primary-foreground font-medium rounded-lg hover:bg-primary/90 disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200"
              >
                <span v-if="!isSubmitting">Отправить заявку</span>
                <span v-else>Отправка...</span>
              </button>
            </div>
          </form>
          
          <!-- Сообщение об успешной отправке -->
          <div v-else class="text-center py-8">
            <div class="w-16 h-16 bg-green-100 text-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-2">Заявка отправлена!</h3>
            <p class="text-muted-foreground mb-4">
              Мы получили вашу заявку и свяжемся с вами в ближайшее время для оказания методической поддержки.
            </p>
            <button
              @click="resetForm"
              class="px-6 py-2 bg-primary text-primary-foreground font-medium rounded-lg hover:bg-primary/90 transition-colors duration-200"
            >
              Отправить еще одну заявку
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.prose {
  color: inherit;
}

.prose p {
  margin-bottom: 1rem;
  line-height: 1.7;
}
</style>
