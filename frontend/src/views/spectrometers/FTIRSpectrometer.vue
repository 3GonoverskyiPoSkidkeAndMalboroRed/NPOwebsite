<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <section class="py-20 px-4 bg-gradient-to-b from-background to-muted/20">
      <div class="max-w-7xl mx-auto">
        <div class="grid lg:grid-cols-2 gap-12 items-center mb-16">
          <div>
            <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text">
              СПЕКТРОМЕТР ИК-Фурье
            </h1>
            <p class="text-xl text-muted-foreground mb-8">
              Инфракрасный спектрометр Фурье для молекулярного анализа и идентификации соединений
            </p>
            <div class="flex flex-col sm:flex-row gap-4">
              <Button size="lg" class="px-8">
                Получить консультацию
              </Button>
              <Button variant="outline" size="lg" class="px-8">
                Скачать каталог
              </Button>
            </div>
          </div>
          <div class="relative">
            <img 
              src="/spectroscan-msw.jpg" 
              alt="СПЕКТРОМЕТР ИК-Фурье" 
              class="w-full h-auto rounded-lg shadow-lg"
            />
          </div>
        </div>

        <!-- Второй большой блок: Подвкладки -->
        <section class="py-20 px-4 bg-muted/30">
          <div class="max-w-7xl mx-auto">
            <div class="text-center mb-12">
              <h2 class="text-3xl md:text-4xl font-bold mb-4">
                Подробная информация
              </h2>
            </div>

            <!-- Навигация по вкладкам -->
            <div class="flex flex-wrap justify-center gap-2 mb-12">
              <Button 
                v-for="tab in tabs" 
                :key="tab.id"
                :variant="activeTab === tab.id ? 'default' : 'outline'"
                @click="activeTab = tab.id"
                class="min-w-[120px]"
              >
                {{ tab.label }}
              </Button>
            </div>

            <!-- Контент вкладок -->
            <div class="bg-background rounded-2xl p-8 shadow-sm">
              <!-- Описание -->
              <div v-if="activeTab === 'description'" class="space-y-6">
                <h3 class="text-2xl font-bold mb-4">Описание</h3>
                <div class="prose prose-lg max-w-none">
                  <p>
                    СПЕКТРОМЕТР ИК-Фурье — высокоточный прибор для молекулярного анализа органических и неорганических соединений. Прибор использует технологию преобразования Фурье для получения высококачественных инфракрасных спектров.
                  </p>
                  <p>
                    Анализатор обеспечивает быструю идентификацию соединений, контроль качества материалов и структурный анализ молекул. Широкий спектральный диапазон позволяет анализировать различные типы образцов.
                  </p>
                  <p>
                    Современное программное обеспечение включает обширные библиотеки спектров для автоматической идентификации соединений и количественного анализа.
                  </p>
                </div>
              </div>

              <!-- Характеристики -->
              <div v-if="activeTab === 'specifications'" class="space-y-6">
                <h3 class="text-2xl font-bold mb-4">Характеристики</h3>
                
                <!-- Аналитические параметры -->
                <div class="space-y-4">
                  <h4 class="text-lg font-semibold">АНАЛИТИЧЕСКИЕ ПАРАМЕТРЫ</h4>
                  <div class="grid md:grid-cols-2 gap-6">
                    <div class="space-y-3">
                      <div class="flex justify-between">
                        <span class="font-medium">Спектральный диапазон:</span>
                        <span>4000-400 см⁻¹</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Разрешение:</span>
                        <span>0,25 см⁻¹</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Точность волновых чисел:</span>
                        <span>±0,01 см⁻¹</span>
                      </div>
                    </div>
                    <div class="space-y-3">
                      <div class="flex justify-between">
                        <span class="font-medium">Время сканирования:</span>
                        <span>1-30 секунд</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Соотношение сигнал/шум:</span>
                        <span>50000:1</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Точность пропускания:</span>
                        <span>±0,1%</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Технические характеристики -->
                <div class="space-y-4">
                  <h4 class="text-lg font-semibold">ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</h4>
                  <div class="grid md:grid-cols-2 gap-6">
                    <div class="space-y-3">
                      <div class="flex justify-between">
                        <span class="font-medium">Тип прибора:</span>
                        <span>ИК-Фурье спектрометр</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Источник излучения:</span>
                        <span>Глобар</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Детектор:</span>
                        <span>DTGS</span>
                      </div>
                    </div>
                    <div class="space-y-3">
                      <div class="flex justify-between">
                        <span class="font-medium">Интерферометр:</span>
                        <span>Мишельсона</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Программное обеспечение:</span>
                        <span>Spectrum One</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Габариты:</span>
                        <span>600×500×300 мм</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Преимущества -->
              <div v-if="activeTab === 'advantages'" class="space-y-6">
                <h3 class="text-2xl font-bold mb-4">Преимущества</h3>
                
                <div class="prose prose-lg max-w-none">
                  <div class="space-y-4">
                    <div class="p-4 bg-muted/30 rounded-lg">
                      <h4 class="font-semibold mb-2">Основные преимущества:</h4>
                      <ul class="space-y-2">
                        <li class="flex items-start gap-2">
                          <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
                          <span>высокое разрешение и точность;</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
                          <span>быстрое сканирование;</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
                          <span>широкий спектральный диапазон;</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
                          <span>автоматическая идентификация;</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
                          <span>обширные библиотеки спектров;</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
                          <span>простота эксплуатации.</span>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Решаемые задачи -->
              <div v-if="activeTab === 'tasks'" class="space-y-6">
                <h3 class="text-2xl font-bold mb-4">Решаемые задачи</h3>
                <div class="space-y-4">
                  <div v-for="task in tasks" :key="task.title" class="p-6 bg-muted/30 rounded-lg">
                    <h4 class="text-lg font-semibold mb-2">{{ task.title }}</h4>
                    <p class="text-muted-foreground">{{ task.description }}</p>
                    <div class="mt-3">
                      <span class="text-sm font-medium text-primary">Применение:</span>
                      <span class="text-sm ml-2">{{ task.application }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- CTA Section -->
        <div class="text-center bg-primary/10 rounded-lg p-8 border border-primary/20">
          <h3 class="text-2xl font-semibold mb-4">Заинтересовал спектрометр?</h3>
          <p class="text-muted-foreground mb-6 max-w-2xl mx-auto">
            Получите подробную консультацию и техническое предложение от наших специалистов
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" class="px-8">
              Получить консультацию
            </Button>
            <Button variant="outline" size="lg" class="px-8">
              Запросить коммерческое предложение
            </Button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Button } from "@/components/ui/button";

// Управление вкладками
const activeTab = ref('description');

const tabs = [
  { id: 'description', label: 'Описание' },
  { id: 'specifications', label: 'Характеристики' },
  { id: 'advantages', label: 'Преимущества' },
  { id: 'tasks', label: 'Задачи' }
];

// Данные для решаемых задач
const tasks = [
  {
    title: "Идентификация органических соединений",
    description: "Быстрая и точная идентификация органических соединений по ИК-спектрам",
    application: "Химические лаборатории, фармацевтические компании"
  },
  {
    title: "Контроль качества полимеров",
    description: "Анализ структуры и состава полимерных материалов",
    application: "Полимерная промышленность, исследовательские центры"
  },
  {
    title: "Анализ фармацевтических препаратов",
    description: "Контроль качества и идентификация активных веществ в лекарственных препаратах",
    application: "Фармацевтические компании, контрольно-аналитические лаборатории"
  }
];
</script>
