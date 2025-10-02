<script setup lang="ts">
import { ref, computed } from 'vue'

// Данные о нормативных документах
const regulations = [
  {
    id: 1,
    code: 'ГОСТ Р 53203-2022',
    title: 'Определение серы методом рентгенофлуоресцентной спектрометрии с дисперсией по длине волны',
    company: 'Спектрон',
    category: 'Сера',
    year: '2022'
  },
  {
    id: 2,
    code: 'ГОСТ Р 52247-2021',
    title: 'Методы определения хлорорганических соединений',
    company: 'Спектрон',
    category: 'Хлорорганические соединения',
    year: '2021'
  },
  {
    id: 3,
    code: 'ГОСТ Р 52660-2006',
    title: 'Метод определения серы рентгенофлоуресцентной спектрометрией с дисперсией по длине волны',
    company: 'Спектрон',
    category: 'Сера',
    year: '2006'
  },
  {
    id: 4,
    code: 'ГОСТ 20068.4-88',
    title: 'Метод рентгеноспектрального флоуресцентного определения алюминия',
    company: 'Спектрон',
    category: 'Алюминий',
    year: '1988'
  },
  {
    id: 5,
    code: 'ГОСТ 25278.15-87',
    title: 'Рентгенофлоуресцентный метод определения Zr, Mo, W и Ta в сплавах на основе ниобия',
    company: 'Спектрон',
    category: 'Металлы',
    year: '1987'
  },
  {
    id: 6,
    code: 'ГОСТ 28033-89',
    title: 'Метод рентгенофлоуресцентного анализа стали',
    company: 'Спектрон',
    category: 'Сталь',
    year: '1989'
  },
  {
    id: 7,
    code: 'ГОСТ 28817-90',
    title: 'Рентгенофлоуресцентный метод определения металлов',
    company: 'Спектрон',
    category: 'Металлы',
    year: '1990'
  },
  {
    id: 8,
    code: 'ГОСТ 30608-98',
    title: 'Метод рентгенофлоуресцентного анализа оловянных бронз',
    company: 'Спектрон',
    category: 'Бронзы',
    year: '1998'
  },
  {
    id: 9,
    code: 'ГОСТ 30609-98',
    title: 'Метод рентгенофлоуресцентного анализа литейных латуней',
    company: 'Спектрон',
    category: 'Латуни',
    year: '1998'
  },
  {
    id: 10,
    code: 'ГОСТ Р 51947-2002',
    title: 'Определение серы методом энергодисперсионной рентгенофлоуресцентной спектрометрии',
    company: 'Спектрон',
    category: 'Сера',
    year: '2002'
  },
  {
    id: 11,
    code: 'ГОСТ Р ИСО 20847',
    title: 'Определение серы в топливах методом ренгтенофлоуресцентной энергодисперсионной спектрометрии',
    company: 'Спектрон',
    category: 'Топлива',
    year: 'ISO'
  },
  {
    id: 12,
    code: 'ГОСТ Р ЕН ИСО 14596-2008',
    title: 'Определение содержания серы методом ренгтенофлоуресцентной спектрометрии с дисперсией по длине волны',
    company: 'Спектрон',
    category: 'Сера',
    year: '2008'
  },
  {
    id: 13,
    code: 'ГОСТ Р 54278-2010',
    title: 'Методы определения свинца ренгеновской спектроскопией',
    company: 'Спектрон',
    category: 'Свинец',
    year: '2010'
  }
]

// Фильтры
const selectedCategory = ref('all')
const searchQuery = ref('')

// Получение уникальных категорий
const categories = computed(() => {
  const cats = [...new Set(regulations.map(r => r.category))]
  return ['all', ...cats]
})

// Фильтрация документов
const filteredRegulations = computed(() => {
  let filtered = regulations

  // Фильтр по категории
  if (selectedCategory.value !== 'all') {
    filtered = filtered.filter(r => r.category === selectedCategory.value)
  }

  // Поиск по тексту
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(r => 
      r.code.toLowerCase().includes(query) ||
      r.title.toLowerCase().includes(query) ||
      r.category.toLowerCase().includes(query)
    )
  }

  return filtered
})

// Сортировка по году (новые сначала)
const sortedRegulations = computed(() => {
  return [...filteredRegulations.value].sort((a, b) => {
    if (a.year === 'ISO') return 1
    if (b.year === 'ISO') return -1
    return parseInt(b.year) - parseInt(a.year)
  })
})
</script>

<template>
  <div class="min-h-screen bg-background">
    <!-- Заголовок страницы -->
    <div class="bg-primary/5 py-16 sm:py-20">
      <div class="container px-4 sm:px-6 lg:px-8">
        <div class="max-w-4xl mx-auto text-center">
          <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold mb-4">
            Нормативные документы
          </h1>
          <p class="text-lg sm:text-xl text-muted-foreground max-w-2xl mx-auto">
            ГОСТы и стандарты для рентгенофлуоресцентного анализа, разработанные с участием НПО «СПЕКТРОН»
          </p>
        </div>
      </div>
    </div>

    <!-- Основной контент -->
    <div class="container px-4 sm:px-6 lg:px-8 py-16">
      <div class="max-w-6xl mx-auto">
        
        <!-- Введение -->
        <div class="prose prose-sm sm:prose-base lg:prose-lg max-w-none mb-12">
          <div class="bg-muted/50 p-6 rounded-lg">
            <p class="text-lg font-medium mb-4">
              НПО «СПЕКТРОН» принимает активное участие в разработке нормативных документов и стандартов для рентгенофлуоресцентного анализа. 
              Наши специалисты являются авторами и соавторами множества ГОСТов, обеспечивающих стандартизацию методов анализа.
            </p>
            <p class="text-lg">
              Все представленные документы прошли процедуру утверждения и являются действующими стандартами Российской Федерации.
            </p>
          </div>
        </div>

        <!-- Фильтры и поиск -->
        <div class="mb-8">
          <div class="bg-muted/50 p-6 rounded-lg">
            <div class="grid md:grid-cols-2 gap-6">
              <!-- Поиск -->
              <div>
                <label for="search" class="block text-sm font-medium mb-2">Поиск по документам</label>
                <div class="relative">
                  <input
                    id="search"
                    v-model="searchQuery"
                    type="text"
                    placeholder="Введите код ГОСТ или название..."
                    class="w-full px-4 py-2 pl-10 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  />
                  <svg class="absolute left-3 top-2.5 h-5 w-5 text-muted-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                  </svg>
                </div>
              </div>
              
              <!-- Фильтр по категории -->
              <div>
                <label for="category" class="block text-sm font-medium mb-2">Категория</label>
                <select
                  id="category"
                  v-model="selectedCategory"
                  class="w-full px-4 py-2 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                >
                  <option value="all">Все категории</option>
                  <option v-for="category in categories.slice(1)" :key="category" :value="category">
                    {{ category }}
                  </option>
                </select>
              </div>
            </div>
          </div>
        </div>

        <!-- Статистика -->
        <div class="grid md:grid-cols-4 gap-4 mb-8">
          <div class="bg-primary/10 p-4 rounded-lg text-center">
            <div class="text-2xl font-bold text-primary mb-1">{{ regulations.length }}</div>
            <div class="text-sm text-muted-foreground">Всего документов</div>
          </div>
          <div class="bg-primary/10 p-4 rounded-lg text-center">
            <div class="text-2xl font-bold text-primary mb-1">{{ categories.length - 1 }}</div>
            <div class="text-sm text-muted-foreground">Категорий</div>
          </div>
          <div class="bg-primary/10 p-4 rounded-lg text-center">
            <div class="text-2xl font-bold text-primary mb-1">{{ filteredRegulations.length }}</div>
            <div class="text-sm text-muted-foreground">Найдено</div>
          </div>
          <div class="bg-primary/10 p-4 rounded-lg text-center">
            <div class="text-2xl font-bold text-primary mb-1">{{ regulations.filter(r => r.year >= '2020').length }}</div>
            <div class="text-sm text-muted-foreground">Современных</div>
          </div>
        </div>

        <!-- Список документов -->
        <div class="space-y-4">
          <div
            v-for="regulation in sortedRegulations"
            :key="regulation.id"
            class="bg-background border border-border rounded-lg p-6 hover:shadow-md transition-shadow duration-200"
          >
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
              <div class="flex-1">
                <div class="flex items-center gap-3 mb-2">
                  <span class="bg-primary text-primary-foreground px-3 py-1 rounded-full text-sm font-medium">
                    {{ regulation.code }}
                  </span>
                  <span class="bg-muted text-muted-foreground px-2 py-1 rounded text-xs">
                    {{ regulation.year }}
                  </span>
                  <span class="bg-primary/10 text-primary px-2 py-1 rounded text-xs">
                    {{ regulation.category }}
                  </span>
                </div>
                
                <h3 class="text-lg font-semibold mb-2 text-foreground">
                  {{ regulation.title }}
                </h3>
                
                <div class="flex items-center text-sm text-muted-foreground">
                  <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                  </svg>
                  <span>Разработано: {{ regulation.company }}</span>
                </div>
              </div>
              
              <div class="flex gap-2">
                <button class="px-4 py-2 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90 transition-colors text-sm">
                  <svg class="w-4 h-4 mr-2 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  Скачать
                </button>
                <button class="px-4 py-2 border border-border rounded-lg hover:bg-muted transition-colors text-sm">
                  <svg class="w-4 h-4 mr-2 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                  Подробнее
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Сообщение если ничего не найдено -->
        <div v-if="filteredRegulations.length === 0" class="text-center py-12">
          <div class="w-16 h-16 bg-muted text-muted-foreground rounded-full flex items-center justify-center mx-auto mb-4">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <h3 class="text-lg font-semibold mb-2">Документы не найдены</h3>
          <p class="text-muted-foreground mb-4">
            Попробуйте изменить параметры поиска или выберите другую категорию.
          </p>
          <button 
            @click="searchQuery = ''; selectedCategory = 'all'"
            class="px-4 py-2 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90 transition-colors"
          >
            Сбросить фильтры
          </button>
        </div>

        <!-- Дополнительная информация -->
        <div class="mt-12 bg-muted/50 p-6 rounded-lg">
          <h2 class="text-xl font-semibold mb-4 text-center">Дополнительная информация</h2>
          <div class="grid md:grid-cols-2 gap-6">
            <div>
              <h3 class="font-semibold mb-2">Получение документов</h3>
              <p class="text-sm text-muted-foreground mb-4">
                Для получения полных текстов ГОСТов и стандартов обращайтесь в нашу методическую лабораторию.
              </p>
              <div class="space-y-2">
                <div class="flex items-center text-sm">
                  <span class="text-primary mr-2">•</span>
                  <span>Электронная почта: service@spectronxray.ru</span>
                </div>
                <div class="flex items-center text-sm">
                  <span class="text-primary mr-2">•</span>
                  <span>Телефон: +7 (812) 458-99-99</span>
                </div>
              </div>
            </div>
            
            <div>
              <h3 class="font-semibold mb-2">Методическая поддержка</h3>
              <p class="text-sm text-muted-foreground mb-4">
                Наши специалисты помогут с внедрением стандартов и разработкой собственных методик анализа.
              </p>
              <div class="space-y-2">
                <div class="flex items-center text-sm">
                  <span class="text-primary mr-2">•</span>
                  <span>Консультации по применению стандартов</span>
                </div>
                <div class="flex items-center text-sm">
                  <span class="text-primary mr-2">•</span>
                  <span>Разработка методик под ваши задачи</span>
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

.prose p {
  margin-bottom: 1rem;
  line-height: 1.7;
}
</style>
