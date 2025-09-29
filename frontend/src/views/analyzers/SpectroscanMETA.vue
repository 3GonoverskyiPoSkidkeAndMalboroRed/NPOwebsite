<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <section class="py-20 px-4 bg-gradient-to-b from-background to-muted/20">
      <div class="max-w-7xl mx-auto">
        <div class="grid lg:grid-cols-2 gap-12 items-center mb-16">
          <div>
            <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text">
              СПЕКТРОСКАН МЕТА
            </h1>
            <p class="text-xl text-muted-foreground mb-8">
              Элементный анализатор для определения серы и азота методом УФ-флуоресценции
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
              alt="СПЕКТРОСКАН МЕТА" 
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
                    СПЕКТРОСКАН МЕТА — элементный анализатор для определения серы и азота методом УФ-флуоресценции и хемилюминесценции. Прибор предназначен для анализа газов, жидкостей и биологических материалов.
                  </p>
                  <p>
                    Анализатор использует современные методы УФ-флуоресценции для определения серы и хемилюминесценции для определения азота, обеспечивая высокую точность и чувствительность измерений.
                  </p>
                  <p>
                    Конструкция анализатора позволяет использовать его в различных областях: от анализа газов до биологических материалов.
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
                        <span class="font-medium">Определяемые элементы:</span>
                        <span>Сера (S), Азот (N)</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Метод для серы:</span>
                        <span>УФ-флуоресценция</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Метод для азота:</span>
                        <span>Хемилюминесценция</span>
                      </div>
                    </div>
                    <div class="space-y-3">
                      <div class="flex justify-between">
                        <span class="font-medium">Тип проб:</span>
                        <span>Газы, жидкости, биоматериалы</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Время анализа:</span>
                        <span>3-5 минут</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Точность:</span>
                        <span>±0.01% масс.</span>
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
                        <span class="font-medium">Тип анализатора:</span>
                        <span>Элементный</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Кюветы:</span>
                        <span>Ø32 мм, V 8 см³</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Мощность рентгеновской трубки:</span>
                        <span>до 200 Вт</span>
                      </div>
                    </div>
                    <div class="space-y-3">
                      <div class="flex justify-between">
                        <span class="font-medium">Программное обеспечение:</span>
                        <span>Спектр-Квант</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Габаритные размеры:</span>
                        <span>530×480×340 мм</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="font-medium">Масса:</span>
                        <span>40 кг</span>
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
                          <span>УФ-флуоресценция для серы;</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
                          <span>хемилюминесценция для азота;</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
                          <span>анализ газов и жидкостей;</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
                          <span>анализ биологических материалов;</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
                          <span>высокая чувствительность;</span>
                        </li>
                        <li class="flex items-start gap-2">
                          <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
                          <span>широкий спектр применения.</span>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Документация -->
              <div v-if="activeTab === 'documentation'" class="space-y-6">
                <h3 class="text-2xl font-bold mb-4">Документация</h3>
                <div class="grid md:grid-cols-2 gap-6">
                  <div v-for="doc in documentation" :key="doc.name" class="p-4 border rounded-lg hover:bg-muted/50 transition-colors">
                    <div class="flex items-center gap-3">
                      <div class="text-2xl">{{ doc.icon }}</div>
                      <div class="flex-1">
                        <h4 class="font-semibold">{{ doc.name }}</h4>
                        <p class="text-sm text-muted-foreground">{{ doc.description }}</p>
                      </div>
                      <Button variant="outline" size="sm">
                        Скачать
                      </Button>
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

              <!-- Материалы -->
              <div v-if="activeTab === 'materials'" class="space-y-6">
                <h3 class="text-2xl font-bold mb-4">Материалы</h3>
                
                <div class="prose prose-lg max-w-none">
                  <ul class="space-y-2">
                    <li>Охлаждающая жидкость 500 мл</li>
                    <li>Пипетка Пастера</li>
                    <li>Пленка полиэтилентерефталатная 3,0 мкм (рулон 100 м)</li>
                    <li>Кювета вентилируемая диаметр 32 мм (упаковка 100 шт)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (5 ppm)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (0,0%)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (10 ppm)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (25 ppm)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (50 ppm)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (100 ppm)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (300 ppm)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (600 ppm)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (0,1%)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (0,2%)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (0,5%)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (1,0%)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (2,0%)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (4,0%)</li>
                    <li>Стандартный образец массовой доли серы в минеральном масле (5,0%)</li>
                    <li>Стандартный образец массовой доли азота в минеральном масле (5 ppm)</li>
                    <li>Стандартный образец массовой доли азота в минеральном масле (0,0%)</li>
                    <li>Стандартный образец массовой доли азота в минеральном масле (10 ppm)</li>
                    <li>Стандартный образец массовой доли азота в минеральном масле (25 ppm)</li>
                    <li>Стандартный образец массовой доли азота в минеральном масле (50 ppm)</li>
                    <li>Стандартный образец массовой доли азота в минеральном масле (100 ppm)</li>
                    <li>Термобумага для принтера</li>
                    <li>Узел щели входной</li>
                    <li>Образец для настройки KCl</li>
                    <li>Образец для настройки GR</li>
                    <li>Образец для настройки KO-D3</li>
                    <li>Образец для настройки КО-91</li>
                  </ul>
                  
                  <div class="mt-8 p-6 bg-primary/5 rounded-lg border border-primary/20">
                    <h4 class="text-lg font-semibold text-primary mb-4">ТЕЛЕФОН ДЛЯ ЗАКАЗА РАСХОДНЫХ МАТЕРИАЛОВ</h4>
                    <p><strong>Телефон:</strong> +7 (812) 324-15-92</p>
                    <p><strong>WhatsApp / Telegram / Viber:</strong> +7 (901) 304-44-44</p>
                    <p><strong>E-mail:</strong> service@spectronxray.ru</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- CTA Section -->
        <div class="text-center bg-primary/10 rounded-lg p-8 border border-primary/20">
          <h3 class="text-2xl font-semibold mb-4">Заинтересовал анализатор?</h3>
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
  { id: 'documentation', label: 'Документация' },
  { id: 'tasks', label: 'Задачи' },
  { id: 'materials', label: 'Материалы' }
];

// Данные для документации
const documentation = [
  {
    name: "Руководство пользователя",
    description: "Подробное руководство по эксплуатации прибора",
    icon: "📖"
  },
  {
    name: "Технический паспорт",
    description: "Технические характеристики и параметры",
    icon: "📋"
  },
  {
    name: "Сертификат соответствия",
    description: "Документ о соответствии стандартам",
    icon: "📜"
  },
  {
    name: "Инструкция по безопасности",
    description: "Правила безопасной эксплуатации",
    icon: "⚠️"
  }
];

// Данные для решаемых задач
const tasks = [
  {
    title: "Анализ газов и жидкостей",
    description: "Определение содержания серы и азота в газовых и жидких пробах с использованием современных методов",
    application: "Химические лаборатории, газовые компании"
  },
  {
    title: "Анализ биологических материалов",
    description: "Определение элементного состава биологических материалов для научных исследований",
    application: "Биологические лаборатории, научно-исследовательские институты"
  },
  {
    title: "Элементный анализ",
    description: "Комплексный элементный анализ различных типов проб с высокой точностью",
    application: "Аналитические лаборатории, сертификационные центры"
  }
];
</script>
