<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

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

// Данные сервисных центров
const serviceCenters = ref([
  { id: 1, city: 'Екатеринбург', name: 'ООО «Экоприбор-Сервис»', address: 'РФ, Свердловская обл., г. Екатеринбург, ул. Сибирский тракт, д. 57, офис 309', email: 'info@gcpro.ru', phone: '+7 (343) 300-90-95', lat: 56.8431, lng: 60.6454 },
  { id: 2, city: 'Казань', name: 'ООО НПФ "Экрос Инжиниринг"', address: 'РФ, Республика Татарстан, г. Казань, ул. Родины, дом № 7', email: 'ecros.kazan@mail.ru', phone: '+7 (843) 277-57-01', lat: 55.8304, lng: 49.0661 },
  { id: 3, city: 'Краснодар', name: 'ИП Барбанаков Андрей Викторович', address: 'РФ. Краснодарский край, г. Краснодар', email: 'rempriborkrd@mail.ru', phone: '+7-909-456-71-25', lat: 45.0448, lng: 38.976 },
  { id: 4, city: 'Краснодар', name: 'ООО "РЕМКИПЭЛЕКТРОНАЛАДКА" / ИП ЛЕОНОВ В.А.', address: 'РФ, Краснодарский край, г. Краснодар', email: 'remkip@mail.ru', phone: '+7(918) 11-27-127', lat: 45.0448, lng: 38.976 },
  { id: 5, city: 'Минск', name: 'ООО "Эмпрос"', address: 'Республика Беларусь, г. Минск, ул. Маяковского, д. 111, комн. 303', email: 'info@mce.by', phone: '+375(33) 680-98-22', lat: 53.9045, lng: 27.5615 },
  { id: 6, city: 'Москва', name: 'ИП Сахаров Виталий Александрович', address: 'РФ, г. Москва', email: 'ipvs.engineer@gmail.com', phone: '+7 (904) 338-14-31', lat: 55.7558, lng: 37.6176 },
  { id: 7, city: 'Москва', name: 'ООО "Соктрейд Сервис"', address: 'РФ, Москва, ул. Шаболовка, 31Г, подъезд 1', email: 'info@soctrade-service.com', phone: '+7 (495) 230-31-69', lat: 55.7558, lng: 37.6176 },
  { id: 8, city: 'Нижневартовск', name: 'ИП Чупин Андрей Александрович', address: 'РФ, ХМАО, г. Нижневартовск', email: 'chypaishim@mail.ru', phone: '+7-912-999-07-89', lat: 60.9394, lng: 76.5694 },
  { id: 9, city: 'Новосибирск', name: 'ООО «Лабораторный Сервис Сибири»', address: 'РФ, Новосибирская область, г. Новосибирск, проезд Электрозаводской, зд. 1/1, офис 4', email: 'info@lss-lab.ru', phone: '+7 (383) 322-54-05', lat: 55.0084, lng: 82.9357 },
  { id: 10, city: 'Новосибирск', name: 'ООО "СПЕКТРОМАРТ"', address: 'РФ, Новосибирская обл, Новосибирск, Пролетарская, дом № 271/3, оф.1', email: 'info@spectromart.ru', phone: '+7-383-312-01-37', lat: 55.0084, lng: 82.9357 },
  { id: 11, city: 'Одинцово', name: 'ООО "СК Альянс"', address: 'РФ, Московская обл., Одинцово г., Маршала Крылова б-р, дом 25А, этаж 2, пом. 12, комната 29', email: 'as@scalianz.ru', phone: '+7 (915) 099-18-51', lat: 55.6759, lng: 37.2789 },
  { id: 12, city: 'Омск', name: 'ООО "Экопроектсервис"', address: 'РФ, Омская обл., г. Омск, ул. 20 Партсъезда, дом № 49', email: 'info@epsomsk.ru', phone: '+7 (3812) 72-96-99', lat: 54.9885, lng: 73.3242 },
  { id: 13, city: 'Омск', name: 'АО "ЭПАК-Сервис"', address: 'РФ, Омская обл, г. Омск, улица Нагибина, 1', email: 'epac@epac-service.ru', phone: '+7 (3812) 43-38-84', lat: 54.9885, lng: 73.3242 },
  { id: 14, city: 'Омск', name: 'ИП Исмакаев Марсель Камильевич', address: 'РФ, Омская обл, г. Омск', email: 'imk@imk-service.ru', phone: '+7-913-977-20-41', lat: 54.9885, lng: 73.3242 },
  { id: 15, city: 'Омск', name: 'ООО "АналитПромСервис"', address: 'РФ, Омская обл, Омск г, Заводская 1-я ул, дом № 2, оф.15', email: 'aps@sibaps.ru', phone: '+7 (3812) 21-77-27', lat: 54.9885, lng: 73.3242 },
  { id: 16, city: 'Самара', name: 'ООО «ЛАБКОМПЛЕКТ-СЕРВИС»', address: 'РФ, Самарская обл., г. Самара, ул. Николая Панова, дом № 50 секция 8, 2-й этаж', email: 'labkomplekt@gmail.com', phone: '+7 (846) 212-07-78', lat: 53.2001, lng: 50.15 },
  { id: 17, city: 'Самара', name: 'ООО "ЛАБЭКС"', address: 'РФ, Самарская обл, г. Самара, ул. Ново-Садовая, д.106, корп. 170, к. 48', email: 'labxservice@gmail.com', phone: '+7-(927) 702-20-92', lat: 53.2001, lng: 50.15 },
  { id: 18, city: 'Санкт-Петербург', name: 'ИП Сахаров Виталий Александрович', address: 'РФ, г. Санкт-Петербург', email: 'ipvs.engineer@gmail.com', phone: '+7 (904) 338-14-31', lat: 59.9311, lng: 30.3609 },
  { id: 19, city: 'Санкт-Петербург', name: 'АО "НеваЛаб"', address: 'РФ, г. Санкт-Петербург, Московское шоссе, д. 46', email: 'info@nevalab.ru', phone: '+7 (812) 336-32-00', lat: 59.9311, lng: 30.3609 },
  { id: 20, city: 'Санкт-Петербург', name: 'ООО "ТрансАналит"', address: 'РФ, г. Санкт-Петербург, ул. Уральская, д. 13, лит А, пом.58', email: 'info@transanalit.ru', phone: '+7 (812) 300-60-00', lat: 59.9311, lng: 30.3609 },
  { id: 21, city: 'Тюмень', name: 'ФБУ "Тюменский ЦСМ"', address: 'РФ, Тюменская обл., г.Тюмень, ул. Минская, д. 88', email: '501@csm72.ru', phone: '8(3452)59-29-37', lat: 57.1522, lng: 65.5272 },
  { id: 22, city: 'Уральск', name: 'ТОО "Топан"', address: 'Республика Казахстан, Западно-Казахстанская область, г.Уральск, ул.Ружейникова, 11', email: 'info@topan.kz', phone: '8-(7112) 28-41-02', lat: 51.2278, lng: 51.3865 },
  { id: 23, city: 'Усинск', name: 'ИП Дедюхин Александр Викторович', address: 'РФ, Республика Коми, г. Усинск', email: 'cuser340@rambler.ru', phone: '+7 (912) 956-70-81', lat: 66.0000, lng: 57.5570 },
  { id: 24, city: 'Уфа', name: 'АО «ХИМРЕАКТИВСНАБ»', address: 'РФ, Республика Башкортостан, г. Уфа, ул. Пархоменко, дом № 156/2', email: 'service@chemical.ru', phone: '+7 (347) 292-10-13', lat: 54.7388, lng: 55.9721 }
])

let map: L.Map | null = null

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

// Инициализация карты
const initMap = async () => {
  await nextTick()
  
  if (map) {
    map.remove()
  }
  
  // Создаем иконку для маркеров
  const customIcon = L.icon({
    iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  })
  
  // Создаем карту
  map = L.map('service-centers-map').setView([55.7558, 37.6176], 4)
  
  // Добавляем слой карты
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map)
  
  // Добавляем маркеры для каждого сервисного центра
  serviceCenters.value.forEach(center => {
    L.marker([center.lat, center.lng], { icon: customIcon })
      .addTo(map!)
      .bindPopup(`
        <div class="p-2">
          <h3 class="font-semibold text-sm mb-1">${center.name}</h3>
          <p class="text-xs text-gray-600 mb-1">${center.city}</p>
          <p class="text-xs mb-1">${center.address}</p>
          <p class="text-xs mb-1">
            <a href="mailto:${center.email}" class="text-blue-600 hover:underline">${center.email}</a>
          </p>
          <p class="text-xs">
            <a href="tel:${center.phone}" class="text-blue-600 hover:underline">${center.phone}</a>
          </p>
        </div>
      `)
  })
}

onMounted(() => {
  initMap()
})
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
          
          <div class="grid md:grid-cols-3 gap-6 mb-12">
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

          <!-- Карта сервисных центров -->
          <div class="mb-12">
            <h3 class="text-xl font-bold mb-6 text-center">Карта сервисных центров</h3>
            <div id="service-centers-map" class="w-full h-96 rounded-lg border border-border"></div>
          </div>

          <!-- Список сервисных центров -->
          <div class="mb-12">
            <h3 class="text-xl font-bold mb-6 text-center">Список сервисных центров</h3>
            <div class="overflow-x-auto">
              <table class="w-full border-collapse border border-border rounded-lg">
                <thead>
                  <tr class="bg-muted/50">
                    <th class="border border-border px-4 py-3 text-left font-semibold">Город</th>
                    <th class="border border-border px-4 py-3 text-left font-semibold">Название</th>
                    <th class="border border-border px-4 py-3 text-left font-semibold">Адрес</th>
                    <th class="border border-border px-4 py-3 text-left font-semibold">Эл.почта</th>
                    <th class="border border-border px-4 py-3 text-left font-semibold">Телефон</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="center in serviceCenters" :key="center.id" class="hover:bg-muted/25">
                    <td class="border border-border px-4 py-3 font-medium">{{ center.city }}</td>
                    <td class="border border-border px-4 py-3">{{ center.name }}</td>
                    <td class="border border-border px-4 py-3 text-sm">{{ center.address }}</td>
                    <td class="border border-border px-4 py-3">
                      <a :href="`mailto:${center.email}`" class="text-primary hover:underline">{{ center.email }}</a>
                    </td>
                    <td class="border border-border px-4 py-3">
                      <a :href="`tel:${center.phone}`" class="text-primary hover:underline">{{ center.phone }}</a>
                    </td>
                  </tr>
                </tbody>
              </table>
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
