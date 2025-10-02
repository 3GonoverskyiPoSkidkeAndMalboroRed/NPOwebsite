<script setup lang="ts">
import { ref } from 'vue'

// Активная вкладка
const activeTab = ref('history')

// Список вкладок
const tabs = [
  { id: 'history', name: 'История компании' },
  { id: 'dealers', name: 'Наши дилеры' },
  { id: 'contacts', name: 'Контакты' },
  { id: 'career', name: 'Карьера' },
  { id: 'sout', name: 'СОУТ' }
]

// Функция для переключения вкладок
const setActiveTab = (tabId: string) => {
  activeTab.value = tabId
}
</script>

<template>
  <div class="min-h-screen bg-background">
    <!-- Заголовок страницы -->
    <div class="bg-primary/5 py-16 sm:py-20">
      <div class="container px-4 sm:px-6 lg:px-8">
        <div class="max-w-4xl mx-auto text-center">
          <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold mb-4">
            О компании СПЕКТРОН
          </h1>
          <p class="text-lg sm:text-xl text-muted-foreground max-w-2xl mx-auto">
            Ведущий отечественный производитель аналитического оборудования с 1989 года
          </p>
        </div>
      </div>
    </div>

    <!-- Навигация по вкладкам -->
    <div class="container px-4 sm:px-6 lg:px-8 py-8">
      <div class="max-w-4xl mx-auto">
        <div class="border-b border-border">
          <nav class="-mb-px flex space-x-8 overflow-x-auto">
            <button
              v-for="tab in tabs"
              :key="tab.id"
              @click="setActiveTab(tab.id)"
              :class="[
                'whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm transition-colors duration-200',
                activeTab === tab.id
                  ? 'border-primary text-primary'
                  : 'border-transparent text-muted-foreground hover:text-foreground hover:border-border'
              ]"
            >
              {{ tab.name }}
            </button>
          </nav>
        </div>
      </div>
    </div>

    <!-- Контент вкладок -->
    <div class="container px-4 sm:px-6 lg:px-8 pb-16">
      <div class="max-w-4xl mx-auto">
        
        <!-- История компании -->
        <div v-if="activeTab === 'history'" class="prose prose-sm sm:prose-base lg:prose-lg max-w-none">
          <div class="space-y-6">
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Основание и развитие</h3>
              <p>
                Научно-производственное объединение «СПЕКТРОН» было основано в 1989 году как специализированное предприятие по разработке и производству аналитического оборудования. За более чем 30 лет работы компания стала ведущим отечественным производителем рентгеновских спектрометров и анализаторов.
              </p>
            </div>

            <div class="grid md:grid-cols-2 gap-6">
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">1989-2000</h4>
                <p class="text-sm">Основание компании, первые разработки рентгеновских спектрометров, создание производственной базы в Санкт-Петербурге.</p>
              </div>
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">2000-2010</h4>
                <p class="text-sm">Расширение линейки продукции, выход на международные рынки, получение первых патентов и разработка собственных методик анализа.</p>
              </div>
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">2010-2020</h4>
                <p class="text-sm">Создание сервисной сети по всей России, разработка промышленных решений, получение заключений Минпромторга о российском производстве.</p>
              </div>
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">2020-настоящее время</h4>
                <p class="text-sm">Цифровизация производства, внедрение современных технологий, выпуск свыше 300 приборов ежегодно.</p>
              </div>
            </div>

            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Достижения</h3>
              <ul class="space-y-2">
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Более 50 аттестованных методик анализа</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>5 патентов на изобретения</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Более 100 научных статей</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Внесение в реестры средств измерений 6 стран</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Наши дилеры -->
        <div v-if="activeTab === 'dealers'" class="prose prose-sm sm:prose-base lg:prose-lg max-w-none">
          <div class="space-y-6">
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Сервисная сеть</h3>
              <p>
                НПО «СПЕКТРОН» имеет развитую сеть сервисных центров и дилеров по всей России, обеспечивающую полный спектр услуг по установке, настройке, гарантийному и постгарантийному обслуживанию оборудования.
              </p>
            </div>

            <div class="grid md:grid-cols-2 gap-6">
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Москва</h4>
                <p class="text-sm mb-2">Центральный офис и сервисный центр</p>
                <p class="text-sm text-muted-foreground">ул. Примерная, д. 1, оф. 100</p>
                <p class="text-sm text-muted-foreground">+7 (495) 123-45-67</p>
              </div>
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Санкт-Петербург</h4>
                <p class="text-sm mb-2">Производство и сервисный центр</p>
                <p class="text-sm text-muted-foreground">ул. Производственная, д. 10</p>
                <p class="text-sm text-muted-foreground">+7 (812) 234-56-78</p>
              </div>
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Екатеринбург</h4>
                <p class="text-sm mb-2">Региональный сервисный центр</p>
                <p class="text-sm text-muted-foreground">ул. Уральская, д. 5</p>
                <p class="text-sm text-muted-foreground">+7 (343) 345-67-89</p>
              </div>
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Новосибирск</h4>
                <p class="text-sm mb-2">Региональный сервисный центр</p>
                <p class="text-sm text-muted-foreground">ул. Сибирская, д. 15</p>
                <p class="text-sm text-muted-foreground">+7 (383) 456-78-90</p>
              </div>
            </div>

            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Услуги дилеров</h3>
              <ul class="space-y-2">
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Установка и настройка оборудования</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Гарантийное и постгарантийное обслуживание</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Обучение персонала</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Техническая поддержка</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Поставка расходных материалов</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Контакты -->
        <div v-if="activeTab === 'contacts'" class="prose prose-sm sm:prose-base lg:prose-lg max-w-none">
          <div class="space-y-6">
            <div class="grid md:grid-cols-2 gap-6">
              <div class="bg-muted/50 p-6 rounded-lg">
                <h3 class="text-xl font-semibold mb-4 text-primary">Головной офис</h3>
                <div class="space-y-3">
                  <div>
                    <p class="font-medium">Адрес:</p>
                    <p class="text-sm text-muted-foreground">г. Москва, ул. Примерная, д. 1, оф. 100</p>
                  </div>
                  <div>
                    <p class="font-medium">Телефон:</p>
                    <p class="text-sm text-muted-foreground">+7 (495) 123-45-67</p>
                  </div>
                  <div>
                    <p class="font-medium">Email:</p>
                    <p class="text-sm text-muted-foreground">info@spectron.ru</p>
                  </div>
                </div>
              </div>

              <div class="bg-muted/50 p-6 rounded-lg">
                <h3 class="text-xl font-semibold mb-4 text-primary">Производство</h3>
                <div class="space-y-3">
                  <div>
                    <p class="font-medium">Адрес:</p>
                    <p class="text-sm text-muted-foreground">г. Санкт-Петербург, ул. Производственная, д. 10</p>
                  </div>
                  <div>
                    <p class="font-medium">Телефон:</p>
                    <p class="text-sm text-muted-foreground">+7 (812) 234-56-78</p>
                  </div>
                  <div>
                    <p class="font-medium">Email:</p>
                    <p class="text-sm text-muted-foreground">production@spectron.ru</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Отделы</h3>
              <div class="grid md:grid-cols-2 gap-4">
                <div>
                  <p class="font-medium">Отдел продаж:</p>
                  <p class="text-sm text-muted-foreground">sales@spectron.ru, +7 (495) 123-45-68</p>
                </div>
                <div>
                  <p class="font-medium">Техническая поддержка:</p>
                  <p class="text-sm text-muted-foreground">support@spectron.ru, +7 (495) 123-45-69</p>
                </div>
                <div>
                  <p class="font-medium">Сервисный отдел:</p>
                  <p class="text-sm text-muted-foreground">service@spectron.ru, +7 (495) 123-45-70</p>
                </div>
                <div>
                  <p class="font-medium">Отдел кадров:</p>
                  <p class="text-sm text-muted-foreground">hr@spectron.ru, +7 (495) 123-45-71</p>
                </div>
              </div>
            </div>

            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Режим работы</h3>
              <div class="grid md:grid-cols-2 gap-4">
                <div>
                  <p class="font-medium">Офис:</p>
                  <p class="text-sm text-muted-foreground">Пн-Пт: 9:00-18:00</p>
                </div>
                <div>
                  <p class="font-medium">Сервис:</p>
                  <p class="text-sm text-muted-foreground">Пн-Пт: 8:00-17:00</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Карьера -->
        <div v-if="activeTab === 'career'" class="prose prose-sm sm:prose-base lg:prose-lg max-w-none">
          <div class="space-y-6">
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Работа в НПО «СПЕКТРОН»</h3>
              <p>
                Мы ищем талантливых специалистов, готовых развиваться в области аналитического приборостроения. 
                Наша компания предлагает интересные проекты, профессиональный рост и стабильную работу в динамично развивающейся отрасли.
              </p>
            </div>

            <div class="grid md:grid-cols-2 gap-6">
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Инженер-разработчик</h4>
                <p class="text-sm mb-2">Разработка новых моделей спектрометров</p>
                <ul class="text-sm space-y-1">
                  <li>• Высшее техническое образование</li>
                  <li>• Опыт работы с рентгеновским оборудованием</li>
                  <li>• Знание САПР</li>
                </ul>
              </div>
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Программист</h4>
                <p class="text-sm mb-2">Разработка ПО для аналитического оборудования</p>
                <ul class="text-sm space-y-1">
                  <li>• Опыт программирования на C++/C#</li>
                  <li>• Знание баз данных</li>
                  <li>• Опыт работы с измерительными приборами</li>
                </ul>
              </div>
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Сервисный инженер</h4>
                <p class="text-sm mb-2">Обслуживание и ремонт оборудования</p>
                <ul class="text-sm space-y-1">
                  <li>• Техническое образование</li>
                  <li>• Опыт работы с аналитическим оборудованием</li>
                  <li>• Готовность к командировкам</li>
                </ul>
              </div>
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Менеджер по продажам</h4>
                <p class="text-sm mb-2">Работа с клиентами и развитие продаж</p>
                <ul class="text-sm space-y-1">
                  <li>• Высшее образование</li>
                  <li>• Опыт продаж B2B</li>
                  <li>• Знание аналитического оборудования</li>
                </ul>
              </div>
            </div>

            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Преимущества работы</h3>
              <ul class="space-y-2">
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Конкурентная заработная плата</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Официальное трудоустройство</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Обучение и повышение квалификации</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Дружный коллектив профессионалов</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Интересные и перспективные проекты</span>
                </li>
              </ul>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg text-center">
              <h3 class="text-xl font-semibold mb-4 text-primary">Отправить резюме</h3>
              <p class="mb-4">Отправьте свое резюме на email: hr@spectron.ru</p>
              <a 
                href="mailto:hr@spectron.ru" 
                class="inline-flex items-center px-6 py-3 bg-primary text-primary-foreground font-medium rounded-lg hover:bg-primary/90 transition-colors duration-200"
              >
                Написать нам
              </a>
            </div>
          </div>
        </div>

        <!-- СОУТ -->
        <div v-if="activeTab === 'sout'" class="prose prose-sm sm:prose-base lg:prose-lg max-w-none">
          <div class="space-y-6">
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Специальная оценка условий труда (СОУТ)</h3>
              <p>
                В соответствии с требованиями трудового законодательства РФ, НПО «СПЕКТРОН» проводит специальную оценку условий труда на всех рабочих местах. 
                Это позволяет обеспечить безопасность и комфорт наших сотрудников.
              </p>
            </div>

            <div class="grid md:grid-cols-2 gap-6">
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Цели СОУТ</h4>
                <ul class="text-sm space-y-2">
                  <li>• Идентификация вредных и опасных факторов</li>
                  <li>• Оценка уровня воздействия на работников</li>
                  <li>• Определение класса условий труда</li>
                  <li>• Разработка мероприятий по улучшению условий</li>
                </ul>
              </div>
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Проводимые мероприятия</h4>
                <ul class="text-sm space-y-2">
                  <li>• Аттестация рабочих мест</li>
                  <li>• Измерение физических факторов</li>
                  <li>• Анализ химических факторов</li>
                  <li>• Оценка тяжести и напряженности труда</li>
                </ul>
              </div>
            </div>

            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Результаты СОУТ</h3>
              <div class="grid md:grid-cols-3 gap-4">
                <div class="text-center p-4 bg-background rounded-lg">
                  <div class="text-2xl font-bold text-primary mb-2">95%</div>
                  <div class="text-sm">Рабочих мест с допустимыми условиями</div>
                </div>
                <div class="text-center p-4 bg-background rounded-lg">
                  <div class="text-2xl font-bold text-primary mb-2">5%</div>
                  <div class="text-sm">Рабочих мест с вредными условиями</div>
                </div>
                <div class="text-center p-4 bg-background rounded-lg">
                  <div class="text-2xl font-bold text-primary mb-2">0%</div>
                  <div class="text-sm">Рабочих мест с опасными условиями</div>
                </div>
              </div>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Меры по улучшению условий труда</h3>
              <ul class="space-y-2">
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Установка современной системы вентиляции</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Обеспечение средствами индивидуальной защиты</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Регулярные медицинские осмотры</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Обучение по охране труда</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Мониторинг условий труда</span>
                </li>
              </ul>
            </div>

            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Документы СОУТ</h3>
              <p class="mb-4">Все документы по специальной оценке условий труда доступны для ознакомления:</p>
              <div class="grid md:grid-cols-2 gap-4">
                <div>
                  <p class="font-medium">Отчет о проведении СОУТ:</p>
                  <p class="text-sm text-muted-foreground">Документ содержит результаты оценки всех рабочих мест</p>
                </div>
                <div>
                  <p class="font-medium">Карты СОУТ:</p>
                  <p class="text-sm text-muted-foreground">Индивидуальные карты для каждого рабочего места</p>
                </div>
                <div>
                  <p class="font-medium">Сводная ведомость:</p>
                  <p class="text-sm text-muted-foreground">Обобщенные результаты по всем рабочим местам</p>
                </div>
                <div>
                  <p class="font-medium">План мероприятий:</p>
                  <p class="text-sm text-muted-foreground">Меры по улучшению условий труда</p>
                </div>
              </div>
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

.prose h3 {
  color: inherit;
  margin-top: 0;
  margin-bottom: 1rem;
}

.prose h4 {
  color: inherit;
  margin-top: 0;
  margin-bottom: 0.75rem;
}

.prose p {
  margin-bottom: 1rem;
  line-height: 1.7;
}

.prose ul {
  margin-bottom: 1rem;
}

.prose li {
  margin-bottom: 0.5rem;
}
</style>
