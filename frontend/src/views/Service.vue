<script setup lang="ts">
import { ref } from 'vue'

// Состояние формы
const formData = ref({
  name: '',
  company: '',
  email: '',
  phone: '',
  equipment: '',
  problem: '',
  urgency: 'normal'
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
    name: '',
    company: '',
    email: '',
    phone: '',
    equipment: '',
    problem: '',
    urgency: 'normal'
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
            Сервисное обслуживание
          </h1>
          <p class="text-lg sm:text-xl text-muted-foreground max-w-2xl mx-auto">
            Полное сервисное обслуживание и обеспечение запасными частями на протяжении всего жизненного цикла приборов
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
              НПО «СПЕКТРОН» гарантирует полное сервисное обслуживание и обеспечение запасными частями на протяжении всего жизненного цикла наших приборов.
            </p>
          </div>
        </div>

        <!-- Наши обязательства -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Наши обязательства</h2>
          
          <div class="grid md:grid-cols-3 gap-6">
            <div class="bg-primary/10 p-6 rounded-lg">
              <div class="text-center mb-4">
                <div class="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-3">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <h3 class="text-lg font-semibold mb-3">Гарантия</h3>
              </div>
              <p class="text-sm">
                На всё оборудование устанавливается гарантийный срок не менее 12 месяцев. В этот период НПО «СПЕКТРОН» бесплатно устранит любые возникшие неисправности.
              </p>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <div class="text-center mb-4">
                <div class="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-3">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1" />
                  </svg>
                </div>
                <h3 class="text-lg font-semibold mb-3">Выгодное постгарантийное обслуживание</h3>
              </div>
              <p class="text-sm">
                После окончания гарантии НПО «СПЕКТРОН» предлагает разумные цены на сервисные работы, ремонт и оригинальные запасные части.
              </p>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <div class="text-center mb-4">
                <div class="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-3">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <h3 class="text-lg font-semibold mb-3">Оперативная техническая поддержка</h3>
              </div>
              <p class="text-sm">
                Обязуемся ответить на ваше обращение и связаться с вами для решения любой технической проблемы в течение 24 часов в рабочие дни.
              </p>
            </div>
          </div>
        </div>

        <!-- Контактная информация -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Нужна помощь? Отправьте заявку!</h2>
          
          <div class="bg-muted/50 p-6 rounded-lg mb-8">
            <p class="text-center mb-6">
              Чтобы обратиться в нашу сервисную службу, просто заполните форму на этой странице или свяжитесь с нами другим удобным для вас способом:
            </p>
            
            <div class="grid md:grid-cols-3 gap-6 text-center">
              <div class="bg-background p-4 rounded-lg">
                <div class="w-10 h-10 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-3">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                </div>
                <p class="font-medium mb-1">Электронная почта</p>
                <a href="mailto:service@spectronxray.ru" class="text-primary hover:underline">
                  service@spectronxray.ru
                </a>
              </div>
              
              <div class="bg-background p-4 rounded-lg">
                <div class="w-10 h-10 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-3">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                </div>
                <p class="font-medium mb-1">Телефон</p>
                <a href="tel:+78124589999" class="text-primary hover:underline">
                  +7 (812) 458-99-99
                </a>
              </div>
              
              <div class="bg-background p-4 rounded-lg">
                <div class="w-10 h-10 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-3">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                  </svg>
                </div>
                <p class="font-medium mb-1">Мессенджеры</p>
                <a href="https://wa.me/79013044444" class="text-primary hover:underline">
                  +7 (901) 304-44-44
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Форма заявки -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Заявка в сервисную службу</h2>
          
          <div class="bg-muted/50 p-6 rounded-lg">
            <form @submit="handleSubmit" v-if="!isSubmitted">
              <div class="grid md:grid-cols-2 gap-6 mb-6">
                <div>
                  <label for="name" class="block text-sm font-medium mb-2">Имя *</label>
                  <input
                    id="name"
                    v-model="formData.name"
                    type="text"
                    required
                    class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                    placeholder="Ваше имя"
                  />
                </div>
                
                <div>
                  <label for="company" class="block text-sm font-medium mb-2">Компания</label>
                  <input
                    id="company"
                    v-model="formData.company"
                    type="text"
                    class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                    placeholder="Название компании"
                  />
                </div>
                
                <div>
                  <label for="email" class="block text-sm font-medium mb-2">Email *</label>
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
                  <label for="phone" class="block text-sm font-medium mb-2">Телефон *</label>
                  <input
                    id="phone"
                    v-model="formData.phone"
                    type="tel"
                    required
                    class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                    placeholder="+7 (xxx) xxx-xx-xx"
                  />
                </div>
              </div>
              
              <div class="mb-6">
                <label for="equipment" class="block text-sm font-medium mb-2">Модель оборудования</label>
                <input
                  id="equipment"
                  v-model="formData.equipment"
                  type="text"
                  class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="Например: СПЕКТРОСКАН МСВ"
                />
              </div>
              
              <div class="mb-6">
                <label for="urgency" class="block text-sm font-medium mb-2">Срочность</label>
                <select
                  id="urgency"
                  v-model="formData.urgency"
                  class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                >
                  <option value="low">Низкая</option>
                  <option value="normal">Обычная</option>
                  <option value="high">Высокая</option>
                  <option value="critical">Критическая</option>
                </select>
              </div>
              
              <div class="mb-6">
                <label for="problem" class="block text-sm font-medium mb-2">Описание проблемы *</label>
                <textarea
                  id="problem"
                  v-model="formData.problem"
                  required
                  rows="4"
                  class="w-full px-3 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  placeholder="Подробно опишите возникшую проблему..."
                ></textarea>
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
                Мы получили вашу заявку и свяжемся с вами в течение 24 часов в рабочие дни.
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

        <!-- Сервисные центры -->
        <div>
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Сервисные центры</h2>
          
          <div class="prose prose-sm sm:prose-base lg:prose-lg max-w-none mb-8">
            <p class="text-center mb-6">
              Для вашего удобства и максимальной оперативности НПО «СПЕКТРОН» создало развитую сеть авторизованных сервисных центров в России и за рубежом.
            </p>
            
            <p class="text-center mb-8">
              Все наши партнеры — это проверенные специалисты, которые прошли обучение и подготовку на нашем производстве и имеют сертификаты установленного образца, дающие право проводить полное обслуживание спектрометров и анализаторов «СПЕКТРОСКАН».
            </p>
          </div>
          
          <div class="grid md:grid-cols-3 gap-6">
            <div class="bg-primary/10 p-6 rounded-lg text-center">
              <div class="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <h3 class="text-lg font-semibold mb-3">Быстрая помощь</h3>
              <p class="text-sm">Сервисный инженер всегда находится в вашем регионе.</p>
            </div>
            
            <div class="bg-primary/10 p-6 rounded-lg text-center">
              <div class="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 class="text-lg font-semibold mb-3">Гарантия качества</h3>
              <p class="text-sm">Все работы выполняются по строгим стандартам производителя.</p>
            </div>
            
            <div class="bg-primary/10 p-6 rounded-lg text-center">
              <div class="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
                </svg>
              </div>
              <h3 class="text-lg font-semibold mb-3">Оригинальные запчасти</h3>
              <p class="text-sm">Используются только сертифицированные комплектующие.</p>
            </div>
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
