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

// Типы для вакансий
interface Vacancy {
  title: string
  responsibilities: string[]
  requirements: string[]
  conditions: string[]
}

// Модальное окно для вакансий
const showModal = ref(false)
const selectedVacancy = ref<Vacancy | null>(null)

// Данные о вакансиях
const vacancies: Record<string, Vacancy> = {
  'Менеджер сервисной службы': {
    title: 'Менеджер сервисной службы',
    responsibilities: [
      'Обеспечение эффективного взаимодействия с заказчиками по коммерческим вопросам, связанным с выполнением сервисных работ:',
      'Общение с заказчиками (по телефону, по электронной почте) по поступившим заявкам на выполнение сервисных работ, в т.ч. ведение официальной переписки.',
      'Подготовка и отправка коммерческих предложений на сервисные работы, в .т.ч. расчет стоимости работ по утвержденным прейскурантам на основании полученной от технических специалистов информации.',
      'Согласование с заказчиками коммерческих условий выполнения работ - стоимость, условия оплаты. Взаимодействие с отделом документооборота для контроля процесса согласования и подписания с заказчиками договоров на выполнение сервисных работ.',
      'Подготовка и отправка счетов заказчикам. Получение актов выполненных работ.',
      'Контроль поступления оплат от заказчиков, в т.ч. работа с просроченными платежами (звонки письма).',
      'Ведение отчетности по своей деятельности в информационной системе.'
    ],
    requirements: [
      'Опыт коммерческого документооборота с корпоративными заказчиками.',
      'Практические знания системы закупок крупных предприятий будут значительным преимуществом.',
      'Знание 1С на уровне уверенного пользователя.',
      'Для кандидатов с уверенным знанием английского языка готовы обсуждать индивидуальные условия.'
    ],
    conditions: [
      'Шаговая доступность м. Балтийская.',
      'Официальное оформление, предоставление льгот и гарантий в полном соответствии с ТК РФ.',
      'Пятидневная рабочая неделя, с 9:00 до 18:00.',
      'ДМС после испытательного срока.',
      'Оплачивается больничный.',
      'Отпуск 28 дней.',
      'Безлимитный чай, кофе, уютная обеденная зона.'
    ]
  },
  'Сервисный инженер': {
    title: 'Сервисный инженер',
    responsibilities: [
      'Обслуживание и ремонт спектрометров и анализаторов серии СПЕКТРОСКАН',
      'Проведение пусконаладочных работ на объектах заказчиков',
      'Техническая поддержка клиентов по телефону и электронной почте',
      'Составление технических отчетов о проведенных работах'
    ],
    requirements: [
      'Высшее техническое образование',
      'Опыт работы с аналитическим оборудованием',
      'Готовность к командировкам',
      'Знание английского языка будет преимуществом'
    ],
    conditions: [
      'Официальное трудоустройство',
      'Конкурентная заработная плата',
      'Оплачиваемые командировки',
      'Обучение и повышение квалификации'
    ]
  },
  'Химик-лаборант': {
    title: 'Химик-лаборант',
    responsibilities: [
      'Проведение анализов на спектрометрах',
      'Подготовка проб для анализа',
      'Ведение лабораторной документации',
      'Калибровка и настройка оборудования'
    ],
    requirements: [
      'Высшее химическое образование',
      'Опыт работы в аналитической лаборатории',
      'Знание методов рентгенофлуоресцентного анализа',
      'Внимательность и аккуратность'
    ],
    conditions: [
      'Стабильная работа в научно-производственной компании',
      'Возможность профессионального роста',
      'Современное оборудование',
      'Дружный коллектив'
    ]
  }
}

// Функции для работы с модальным окном
const openModal = (vacancyTitle: string) => {
  selectedVacancy.value = vacancies[vacancyTitle] || {
    title: vacancyTitle,
    responsibilities: ['Информация о вакансии будет добавлена в ближайшее время'],
    requirements: ['Требования уточняются'],
    conditions: ['Условия работы обсуждаются индивидуально']
  }
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
  selectedVacancy.value = null
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
              <h3 class="text-xl font-semibold mb-4 text-primary">История компании</h3>
              <p class="mb-4">
                ООО «НПО «СПЕКТРОН» - Российский производитель спектрометров и анализаторов серии «СПЕКТРОСКАН» с 1989 года. Наши клиенты – предприятия нефтяной промышленности, предприятия газовой промышленности, экспертные лаборатории, экологические лаборатории и другие предприятия. Наша компания расширяет штат и открывает новые вакансии.
              </p>
              <p class="mb-4">
                Научно-производственное объединение «СПЕКТРОН» - это коллектив уникальных специалистов в области рентгеноспектрального анализа, объединяющих в единое целое знания и навыки в области разработки и производства высококлассного оборудования – рентгено-флюоресцентных кристалл-дифракционных и энерго-дисперсионных спектрометров и анализаторов серии «СПЕКТРОСКАН». Среди нас есть специалисты в области физики, точной механики, аналитической химии, пробоподготовки. У нас работают рентгеномеханики, разработчики программного обеспечения, методисты-химики и методисты-аналитики.
              </p>
              <p class="mb-4">
                Итог нашей работы - спектрометры на базе оригинальной светосильной рентгенооптической схемы, позволяющие достигать высоких аналитических параметров, при относительно невысокой стоимости, размерах и мощности. В конструкции приборов применены собственные разработки НПО «СПЕКТРОН», такие как детекторы, кристалл-анализаторы, высокоточные механические устройства – гониометры. Для энерго-дисперсионного анализатора серы запатентована уникальная разработка - боковое расположение пробозагрузочного устройства, что значительно повысило чувствительность прибора и позволило упростить работу с ним.
              </p>
              <p class="mb-4">
                Разработано и аттестовано методическое обеспечение, позволяющее решать самые разнообразные аналитические задачи наших клиентов.
              </p>
              <p class="mb-4">
                Идеология работы НПО «СПЕКТРОН» заключается в комплексном подходе к решению аналитической задачи наших заказчиков. Оборудование поставляется настроенным под конкретные задачи клиента, и снабжёно всем необходимым для начала работы, в том числе методическим и программным обеспечением, дополнительным оборудованием для подготовки проб, необходимыми расходными материалами.
              </p>
              <p>
                Мы осуществляем полную консультационную, методическую и сервисную поддержку в течении всего времени эксплуатации нашего оборудования.
              </p>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Информация о компании</h3>
              <div class="grid md:grid-cols-2 gap-6">
                <div class="space-y-3">
                  <div>
                    <p class="font-medium">Полное наименование организации:</p>
                    <p class="text-sm text-muted-foreground">Общество с ограниченной ответственностью «Научно-производственное объединение «СПЕКТРОН»</p>
                  </div>
                  <div>
                    <p class="font-medium">Краткое наименование организации:</p>
                    <p class="text-sm text-muted-foreground">ООО «НПО «СПЕКТРОН»</p>
                  </div>
                  <div>
                    <p class="font-medium">Юридический адрес:</p>
                    <p class="text-sm text-muted-foreground">РФ, 190020, Санкт-Петербург, ул. Циолковского, д.10, литера А, пом. 203</p>
                  </div>
                  <div>
                    <p class="font-medium">Почтовый адрес:</p>
                    <p class="text-sm text-muted-foreground">РФ, 190020, Санкт-Петербург, Рижский проспект, д. 30, литера А, а/я 9</p>
                  </div>
                  <div>
                    <p class="font-medium">ИНН:</p>
                    <p class="text-sm text-muted-foreground">7826101943</p>
                  </div>
                  <div>
                    <p class="font-medium">КПП:</p>
                    <p class="text-sm text-muted-foreground">783901001</p>
                  </div>
                </div>
                <div class="space-y-3">
                  <div>
                    <p class="font-medium">БИК:</p>
                    <p class="text-sm text-muted-foreground">044030653</p>
                  </div>
                  <div>
                    <p class="font-medium">Р/С:</p>
                    <p class="text-sm text-muted-foreground">40702810055040002141</p>
                  </div>
                  <div>
                    <p class="font-medium">К/С:</p>
                    <p class="text-sm text-muted-foreground">30101810500000000653</p>
                  </div>
                  <div>
                    <p class="font-medium">ОКПО:</p>
                    <p class="text-sm text-muted-foreground">23124704</p>
                  </div>
                  <div>
                    <p class="font-medium">ОКАТО:</p>
                    <p class="text-sm text-muted-foreground">40262000000</p>
                  </div>
                  <div>
                    <p class="font-medium">ОКВЭД (основной):</p>
                    <p class="text-sm text-muted-foreground">26.51.6; 33.20.6</p>
                  </div>
                  <div>
                    <p class="font-medium">ОГРН:</p>
                    <p class="text-sm text-muted-foreground">1027810238279</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Руководство и контакты</h3>
              <div class="grid md:grid-cols-2 gap-6">
                <div class="space-y-3">
                  <div>
                    <p class="font-medium">Генеральный директор:</p>
                    <p class="text-sm text-muted-foreground">КИСЕЛЕВ Павел Петрович</p>
                  </div>
                  <div>
                    <p class="font-medium">Электронная почта:</p>
                    <p class="text-sm text-muted-foreground">info@spectronxray.ru</p>
                  </div>
                </div>
                <div class="space-y-3">
                  <div>
                    <p class="font-medium">Телефон:</p>
                    <p class="text-sm text-muted-foreground">+7 (812) 325-8183</p>
                  </div>
                  <div>
                    <p class="font-medium">Сайт:</p>
                    <p class="text-sm text-muted-foreground">spectronxray.ru</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Наши дилеры -->
        <div v-if="activeTab === 'dealers'" class="prose prose-sm sm:prose-base lg:prose-lg max-w-none">
          <div class="space-y-6">
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Наши дилеры</h3>
              <p>
                Мы приглашаем к сотрудничеству дилеров из разных стран для продвижения нашего аналитического оборудования
              </p>
            </div>

            <div class="space-y-6">
              <!-- Российская Федерация -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Российская Федерация, Республика Татарстан</h4>
                <div class="space-y-2">
                  <p class="font-medium">ООО НПФ «Экрос Инжиниринг»</p>
                  <p class="text-sm text-muted-foreground">420087, Республика Татарстан, город Казань, ул. Родины, д. 7, помещ. 523(23)</p>
                  <p class="text-sm text-muted-foreground">Тел.: +7 843 277-57-01 / 275-83-17</p>
                  <p class="text-sm text-muted-foreground">E-mail: ecros.kazan@mail.ru</p>
                </div>
              </div>

              <!-- Чешская Республика и Словацкая Республика -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Чешская Республика и Словацкая Республика</h4>
                <div class="space-y-2">
                  <p class="font-medium">RMI, s.r.o.</p>
                  <p class="text-sm text-muted-foreground">Pernštýnská 116, 533 41 Lázně Bohdaneč</p>
                  <p class="text-sm text-muted-foreground">Tel.: +420 466 921 404 / 885</p>
                  <p class="text-sm text-muted-foreground">E-mail: sale@rmi.cz</p>
                  <p class="text-sm text-muted-foreground">Web: www.rmi.cz</p>
                </div>
              </div>

              <!-- Филиппины -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Филиппины</h4>
                <div class="space-y-2">
                  <p class="font-medium">CHEMHUB TECHNOLOGIES INC.</p>
                  <p class="text-sm text-muted-foreground">19 Catleya Street, Samama Phase-II, Napindan, Taguig City 1638</p>
                  <p class="text-sm text-muted-foreground">Tel.: +63 2 218-3749 / +63 2 423-5597</p>
                  <p class="text-sm text-muted-foreground">E-mail: sales@chemhub-tech.com</p>
                  <p class="text-sm text-muted-foreground">Web: chemhub-tech.com</p>
                </div>
              </div>

              <!-- Узбекистан -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Узбекистан</h4>
                <div class="space-y-2">
                  <p class="font-medium">ЧП Fortek</p>
                  <p class="text-sm text-muted-foreground">100077, г. Ташкент, Мирзо-Улугбекский р-н, ул. Сайрам, 6-й проезд, д.13А</p>
                  <p class="text-sm text-muted-foreground">Ориентиры: Саларская База, Суд Мирзо-Улугбекского р-на, Райстат управление</p>
                  <p class="text-sm text-muted-foreground">Тел.: +998 (71) 268 57 50, +998 (71) 268 59 64, +998 (71) 268 59 65</p>
                  <p class="text-sm text-muted-foreground">Факс: +998 (71) 267 71 90</p>
                  <p class="text-sm text-muted-foreground">E-mail: office@fortek.uz</p>
                  <p class="text-sm text-muted-foreground">Web: fortek.uz</p>
                </div>
              </div>

              <!-- Казахстан -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Казахстан</h4>
                <div class="space-y-2">
                  <p class="font-medium">ТОО «Топан»</p>
                  <p class="text-sm text-muted-foreground">Уральск, ул. Ружейникова, 11, Казахстан</p>
                  <p class="text-sm text-muted-foreground">Телефон: +7 (7112) 28-41-42 / +7 (7112) 28-11-66 / +7 (7112) 28-40-10</p>
                  <p class="text-sm text-muted-foreground">Сайт: topan.kz</p>
                  <p class="text-sm text-muted-foreground">E-mail: news@topan.kz / info@topan.kz</p>
                </div>
              </div>

              <!-- Греция -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Греция</h4>
                <div class="space-y-2">
                  <p class="font-medium">ALS Analytical Laboratory Systems S.A.</p>
                  <p class="text-sm text-muted-foreground">Thessalias 6 str., 17456, Alimos, Attiki</p>
                  <p class="text-sm text-muted-foreground">Телефон: (+30) 210-6983974</p>
                  <p class="text-sm text-muted-foreground">Факс: (+30) 210-6980822</p>
                  <p class="text-sm text-muted-foreground">Сайт: alssa.gr</p>
                  <p class="text-sm text-muted-foreground">E-mail: info@alssa.gr</p>
                </div>
              </div>

              <!-- Египет -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Египет</h4>
                <div class="space-y-2">
                  <p class="font-medium">Kazan Co</p>
                  <p class="text-sm text-muted-foreground">Dokki, 12311, Giza, Cairo, Egypt</p>
                  <p class="text-sm text-muted-foreground">Телефон: (+2) 010-150-888-99</p>
                  <p class="text-sm text-muted-foreground">WhatsApp: (+2) 010-150-888-99</p>
                  <p class="text-sm text-muted-foreground">E-mail: amr@kazan-eg.com</p>
                </div>
              </div>

              <!-- Шри-Ланка -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Шри-Ланка</h4>
                <div class="space-y-2">
                  <p class="font-medium">Sigma Delta Technologies (Pvt) ltd.</p>
                  <p class="text-sm text-muted-foreground">84, Herman Gmeiner Mawatha, Halpita, Polgasowita. 10320</p>
                  <p class="text-sm text-muted-foreground">Телефон: +(94) 11 262 6175</p>
                  <p class="text-sm text-muted-foreground">Сайт: sigmadeltatechnologies.com</p>
                  <p class="text-sm text-muted-foreground">E-mail: info@sigmadeltatechnologies.com</p>
                </div>
              </div>

              <!-- Южная Корея -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Южная Корея</h4>
                <div class="space-y-2">
                  <p class="font-medium">3H Corp., Ltd</p>
                  <p class="text-sm text-muted-foreground">Woorim Lions Valley 2nd B/D, B-Dong, 1609&1610, 146-8, Sangdaewon-dong, Jungwon-gu, Sungnam-si, Gyeonggi-do, 462120 Korea</p>
                  <p class="text-sm text-muted-foreground">Телефон: 82(0)31-721-0740</p>
                  <p class="text-sm text-muted-foreground">Факс: 82(0)31-721-0741</p>
                  <p class="text-sm text-muted-foreground">Моб: 82(0)10-6249-5942</p>
                  <p class="text-sm text-muted-foreground">Сайт: spectronxray-korea.com</p>
                  <p class="text-sm text-muted-foreground">E-mail: scott@3htech.co.kr</p>
                </div>
              </div>

              <!-- Ирак -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Ирак</h4>
                <div class="space-y-2">
                  <p class="font-medium">Era Technologies Co. Ltd.</p>
                  <p class="text-sm text-muted-foreground">IRAQ-Baghdad-Al-Mansour 14th Ramadan Str.</p>
                  <p class="text-sm text-muted-foreground">Телефон: +9647714321409</p>
                  <p class="text-sm text-muted-foreground">Сайт: eratech-iq.com</p>
                  <p class="text-sm text-muted-foreground">E-mail: eratech@eratech-iq.com</p>
                </div>
              </div>

              <!-- Пакистан -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Пакистан</h4>
                <div class="space-y-2">
                  <p class="font-medium">Medical system solutions (MSS)</p>
                  <p class="text-sm text-muted-foreground">West Land Trade Centre, Suite 615-A, C/5 Block - 7 & 8 Commercial Area K.C.H.S, Shaheed-e-millat Road. Karachi, Pakistan</p>
                  <p class="text-sm text-muted-foreground">Телефон: +92 21 34548101</p>
                  <p class="text-sm text-muted-foreground">Сайт: mss.net.pk</p>
                  <p class="text-sm text-muted-foreground">E-mail: info@mss.net.pk</p>
                </div>
              </div>

              <!-- Республика Беларусь -->
              <div class="bg-primary/10 p-6 rounded-lg">
                <h4 class="text-lg font-semibold mb-3">Республика Беларусь</h4>
                <div class="space-y-2">
                  <p class="font-medium">ООО «ТоталЛаб»</p>
                  <p class="text-sm text-muted-foreground">220028, г. Минск, ул. Маяковского, д. 111, ком. 302/1</p>
                  <p class="text-sm text-muted-foreground">Тел/факс: +375 17 253 44 81</p>
                  <p class="text-sm text-muted-foreground">Сайт: totallab.by</p>
                  <p class="text-sm text-muted-foreground">E-mail: info@totallab.by</p>
                </div>
              </div>
            </div>

            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Сотрудничество</h3>
              <p class="mb-4">
                Если вы заинтересованы в сотрудничестве, свяжитесь с нами:
              </p>
              <div class="space-y-2">
                <p class="font-medium">ООО "НПО "СПЕКТРОН"</p>
                <p class="text-sm text-muted-foreground">190103, Россия, Санкт-Петербург, ул. Циолковского, 10А</p>
                <p class="text-sm text-muted-foreground">т. +7 (812) 325-81-83</p>
                <p class="text-sm text-muted-foreground">ф. +7-812-325-8503</p>
                <p class="text-sm text-muted-foreground">e-mail: info@spectronxray.ru</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Контакты -->
        <div v-if="activeTab === 'contacts'" class="prose prose-sm sm:prose-base lg:prose-lg max-w-none">
          <div class="space-y-6">
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Контактная информация</h3>
              <div class="space-y-4">
                <div>
                  <p class="font-medium">ООО «НПО «СПЕКТРОН»</p>
                </div>
                <div>
                  <p class="font-medium">Фактический адрес:</p>
                  <p class="text-sm text-muted-foreground">Россия, 190020, г. Санкт-Петербург, ул. Циолковского, д. 10, литера А</p>
                </div>
                <div>
                  <p class="font-medium">Почтовый адрес:</p>
                  <p class="text-sm text-muted-foreground">Россия, 190020, г. Санкт-Петербург, Рижский проспект, д. 30, литера А, а/я 57</p>
                </div>
                <div>
                  <p class="font-medium">Телефон:</p>
                  <p class="text-sm text-muted-foreground">+7(812)325-8183</p>
                </div>
                <div>
                  <p class="font-medium">Факс:</p>
                  <p class="text-sm text-muted-foreground">+7(812)325-8503</p>
                </div>
                <div>
                  <p class="font-medium">Электронная почта:</p>
                  <div class="ml-4 space-y-1">
                    <p class="text-sm text-muted-foreground">По общим вопросам: info@spectronxray.ru</p>
                    <p class="text-sm text-muted-foreground">Отдел сервиса: service@spectronxray.ru</p>
                    <p class="text-sm text-muted-foreground">Отдел продаж: rus@spectronxray.ru</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Режим работы</h3>
              <div class="grid md:grid-cols-3 gap-4">
                <div>
                  <p class="font-medium">Рабочее время:</p>
                  <p class="text-sm text-muted-foreground">9:00 – 18:00</p>
                </div>
                <div>
                  <p class="font-medium">Рабочие дни:</p>
                  <p class="text-sm text-muted-foreground">Пн — Пт</p>
                </div>
                <div>
                  <p class="font-medium">Выходные дни:</p>
                  <p class="text-sm text-muted-foreground">Сб — Вс</p>
                </div>
              </div>
            </div>

            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Юридическая информация</h3>
              <div class="grid md:grid-cols-2 gap-6">
                <div class="space-y-3">
                  <div>
                    <p class="font-medium">Полное наименование организации:</p>
                    <p class="text-sm text-muted-foreground">Общество с ограниченной ответственностью «Научно-производственное объединение «СПЕКТРОН»</p>
                  </div>
                  <div>
                    <p class="font-medium">Краткое наименование организации:</p>
                    <p class="text-sm text-muted-foreground">ООО «НПО «СПЕКТРОН»</p>
                  </div>
                  <div>
                    <p class="font-medium">Юридический адрес:</p>
                    <p class="text-sm text-muted-foreground">РФ, 190020, Санкт-Петербург, ул. Циолковского, д. 10, Лит. А</p>
                  </div>
                  <div>
                    <p class="font-medium">Почтовый адрес:</p>
                    <p class="text-sm text-muted-foreground">РФ, 190020, Санкт-Петербург, Рижский проспект, д.30, литера А, а/я 57</p>
                  </div>
                  <div>
                    <p class="font-medium">ИНН:</p>
                    <p class="text-sm text-muted-foreground">7826101943</p>
                  </div>
                  <div>
                    <p class="font-medium">КПП:</p>
                    <p class="text-sm text-muted-foreground">783901001</p>
                  </div>
                </div>
                <div class="space-y-3">
                  <div>
                    <p class="font-medium">БИК:</p>
                    <p class="text-sm text-muted-foreground">044030653</p>
                  </div>
                  <div>
                    <p class="font-medium">Р/С:</p>
                    <p class="text-sm text-muted-foreground">40702810055040002141</p>
                  </div>
                  <div>
                    <p class="font-medium">К/С:</p>
                    <p class="text-sm text-muted-foreground">30101810500000000653</p>
                  </div>
                  <div>
                    <p class="font-medium">ОКПО:</p>
                    <p class="text-sm text-muted-foreground">23124704</p>
                  </div>
                  <div>
                    <p class="font-medium">ОКАТО:</p>
                    <p class="text-sm text-muted-foreground">40262000000</p>
                  </div>
                  <div>
                    <p class="font-medium">ОКВЭД (основной):</p>
                    <p class="text-sm text-muted-foreground">26.51.6; 33.20.6</p>
                  </div>
                  <div>
                    <p class="font-medium">ОГРН:</p>
                    <p class="text-sm text-muted-foreground">1027810238279</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Руководство</h3>
              <div class="grid md:grid-cols-2 gap-6">
                <div class="space-y-3">
                  <div>
                    <p class="font-medium">Генеральный директор:</p>
                    <p class="text-sm text-muted-foreground">КИСЕЛЕВ Павел Петрович</p>
                  </div>
                  <div>
                    <p class="font-medium">Электронная почта:</p>
                    <p class="text-sm text-muted-foreground">info@spectronxray.ru</p>
                  </div>
                </div>
                <div class="space-y-3">
                  <div>
                    <p class="font-medium">Телефон:</p>
                    <p class="text-sm text-muted-foreground">+7(812)325-8183</p>
                  </div>
                  <div>
                    <p class="font-medium">Сайт:</p>
                    <p class="text-sm text-muted-foreground">spectronxray.ru</p>
                  </div>
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
              <p class="mb-4">
                Мы ищем талантливых специалистов, готовых развиваться в области аналитического приборостроения. 
                Наша компания предлагает интересные проекты, профессиональный рост и стабильную работу в динамично развивающейся отрасли.
              </p>
              <p class="mb-4">
                По вопросам трудоустройства обращайтесь по телефону или электронной почте:
              </p>
              <div class="space-y-2">
                <p class="font-medium">Телефон: +7(812)325-8183 (добавочный 203)</p>
                <p class="font-medium">Email: info@spectronxray.ru</p>
              </div>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4 text-primary">Действующие вакансии</h3>
              <div class="grid md:grid-cols-2 gap-4">
                <div class="space-y-3">
                  <div 
                    class="bg-background p-4 rounded-lg cursor-pointer hover:bg-primary/5 transition-colors duration-200 border border-transparent hover:border-primary/20"
                    @click="openModal('Менеджер сервисной службы')"
                  >
                    <h4 class="font-semibold text-primary hover:text-primary/80">Менеджер сервисной службы</h4>
                    <p class="text-sm text-muted-foreground mt-1">Нажмите для подробной информации</p>
                  </div>
                  <div 
                    class="bg-background p-4 rounded-lg cursor-pointer hover:bg-primary/5 transition-colors duration-200 border border-transparent hover:border-primary/20"
                    @click="openModal('Сервисный инженер')"
                  >
                    <h4 class="font-semibold text-primary hover:text-primary/80">Сервисный инженер</h4>
                    <p class="text-sm text-muted-foreground mt-1">Нажмите для подробной информации</p>
                  </div>
                  <div 
                    class="bg-background p-4 rounded-lg cursor-pointer hover:bg-primary/5 transition-colors duration-200 border border-transparent hover:border-primary/20"
                    @click="openModal('Химик-лаборант')"
                  >
                    <h4 class="font-semibold text-primary hover:text-primary/80">Химик-лаборант</h4>
                    <p class="text-sm text-muted-foreground mt-1">Нажмите для подробной информации</p>
                  </div>
                  <div 
                    class="bg-background p-4 rounded-lg cursor-pointer hover:bg-primary/5 transition-colors duration-200 border border-transparent hover:border-primary/20"
                    @click="openModal('Ведущий Инженер-конструктор')"
                  >
                    <h4 class="font-semibold text-primary hover:text-primary/80">Ведущий Инженер-конструктор</h4>
                    <p class="text-sm text-muted-foreground mt-1">Нажмите для подробной информации</p>
                  </div>
                  <div 
                    class="bg-background p-4 rounded-lg cursor-pointer hover:bg-primary/5 transition-colors duration-200 border border-transparent hover:border-primary/20"
                    @click="openModal('Ведущий инженер-электронщик')"
                  >
                    <h4 class="font-semibold text-primary hover:text-primary/80">Ведущий инженер-электронщик</h4>
                    <p class="text-sm text-muted-foreground mt-1">Нажмите для подробной информации</p>
                  </div>
                  <div 
                    class="bg-background p-4 rounded-lg cursor-pointer hover:bg-primary/5 transition-colors duration-200 border border-transparent hover:border-primary/20"
                    @click="openModal('Инженер эмиссионных спектрометров')"
                  >
                    <h4 class="font-semibold text-primary hover:text-primary/80">Инженер эмиссионных спектрометров</h4>
                    <p class="text-sm text-muted-foreground mt-1">Нажмите для подробной информации</p>
                  </div>
                </div>
                <div class="space-y-3">
                  <div 
                    class="bg-background p-4 rounded-lg cursor-pointer hover:bg-primary/5 transition-colors duration-200 border border-transparent hover:border-primary/20"
                    @click="openModal('Инженер-электронщик')"
                  >
                    <h4 class="font-semibold text-primary hover:text-primary/80">Инженер-электронщик</h4>
                    <p class="text-sm text-muted-foreground mt-1">Нажмите для подробной информации</p>
                  </div>
                  <div 
                    class="bg-background p-4 rounded-lg cursor-pointer hover:bg-primary/5 transition-colors duration-200 border border-transparent hover:border-primary/20"
                    @click="openModal('Кладовщик')"
                  >
                    <h4 class="font-semibold text-primary hover:text-primary/80">Кладовщик</h4>
                    <p class="text-sm text-muted-foreground mt-1">Нажмите для подробной информации</p>
                  </div>
                  <div 
                    class="bg-background p-4 rounded-lg cursor-pointer hover:bg-primary/5 transition-colors duration-200 border border-transparent hover:border-primary/20"
                    @click="openModal('Менеджер по продажам')"
                  >
                    <h4 class="font-semibold text-primary hover:text-primary/80">Менеджер по продажам</h4>
                    <p class="text-sm text-muted-foreground mt-1">Нажмите для подробной информации</p>
                  </div>
                  <div 
                    class="bg-background p-4 rounded-lg cursor-pointer hover:bg-primary/5 transition-colors duration-200 border border-transparent hover:border-primary/20"
                    @click="openModal('Радиомонтажник высоковольтных источников питания')"
                  >
                    <h4 class="font-semibold text-primary hover:text-primary/80">Радиомонтажник высоковольтных источников питания</h4>
                    <p class="text-sm text-muted-foreground mt-1">Нажмите для подробной информации</p>
                  </div>
                  <div 
                    class="bg-background p-4 rounded-lg cursor-pointer hover:bg-primary/5 transition-colors duration-200 border border-transparent hover:border-primary/20"
                    @click="openModal('Руководитель продукта')"
                  >
                    <h4 class="font-semibold text-primary hover:text-primary/80">Руководитель продукта</h4>
                    <p class="text-sm text-muted-foreground mt-1">Нажмите для подробной информации</p>
                  </div>
                </div>
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
              <p class="mb-4">Отправьте свое резюме на email: info@spectronxray.ru</p>
              <a 
                href="mailto:info@spectronxray.ru" 
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

    <!-- Модальное окно для вакансий -->
    <div 
      v-if="showModal" 
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm"
      @click="closeModal"
    >
      <div 
        class="bg-background rounded-lg shadow-xl max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto"
        @click.stop
      >
        <div class="p-6">
          <!-- Заголовок модального окна -->
          <div class="flex justify-between items-start mb-6">
            <h2 class="text-2xl font-bold text-primary">{{ selectedVacancy?.title }}</h2>
            <button 
              @click="closeModal"
              class="text-muted-foreground hover:text-foreground transition-colors duration-200 p-2 -m-2"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>

          <!-- Содержимое модального окна -->
          <div class="space-y-6">
            <!-- Обязанности -->
            <div v-if="selectedVacancy?.responsibilities?.length">
              <h3 class="text-lg font-semibold mb-3 text-primary">Обязанности:</h3>
              <ul class="space-y-2">
                <li 
                  v-for="(responsibility, index) in selectedVacancy.responsibilities" 
                  :key="index"
                  class="flex items-start"
                >
                  <span class="text-primary mr-2 flex-shrink-0 mt-1">•</span>
                  <span class="text-sm">{{ responsibility }}</span>
                </li>
              </ul>
            </div>

            <!-- Требования -->
            <div v-if="selectedVacancy?.requirements?.length">
              <h3 class="text-lg font-semibold mb-3 text-primary">Требования:</h3>
              <ul class="space-y-2">
                <li 
                  v-for="(requirement, index) in selectedVacancy.requirements" 
                  :key="index"
                  class="flex items-start"
                >
                  <span class="text-primary mr-2 flex-shrink-0 mt-1">•</span>
                  <span class="text-sm">{{ requirement }}</span>
                </li>
              </ul>
            </div>

            <!-- Условия -->
            <div v-if="selectedVacancy?.conditions?.length">
              <h3 class="text-lg font-semibold mb-3 text-primary">Условия:</h3>
              <ul class="space-y-2">
                <li 
                  v-for="(condition, index) in selectedVacancy.conditions" 
                  :key="index"
                  class="flex items-start"
                >
                  <span class="text-primary mr-2 flex-shrink-0 mt-1">•</span>
                  <span class="text-sm">{{ condition }}</span>
                </li>
              </ul>
            </div>
          </div>

          <!-- Кнопки действий -->
          <div class="flex justify-between items-center mt-8 pt-6 border-t border-border">
            <button 
              @click="closeModal"
              class="px-4 py-2 text-muted-foreground hover:text-foreground transition-colors duration-200"
            >
              Возврат к списку
            </button>
            <a 
              href="mailto:info@spectronxray.ru?subject=Отклик на вакансию: {{ selectedVacancy?.title }}"
              class="inline-flex items-center px-6 py-3 bg-primary text-primary-foreground font-medium rounded-lg hover:bg-primary/90 transition-colors duration-200"
            >
              Откликнуться на вакансию
            </a>
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
