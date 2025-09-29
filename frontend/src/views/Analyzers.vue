<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <section class="py-20 px-4">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text ">
            Анализаторы
          </h1>

        </div>

        <!-- Categories Table -->
        <div class="mb-16">
          <div class="overflow-x-auto">
            <table class="w-full border-collapse border border-border rounded-lg">
              <thead>
                <tr class="bg-muted">
                  <th class="border border-border p-3 text-center">Изображение</th>
                  <th class="border border-border p-3 text-center">Модель</th>
                  <th class="border border-border p-3 text-center">Описание</th>
                  <th class="border border-border p-3 text-center">Решаемые задачи</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="category in categories" :key="category.id" class="hover:bg-muted/50">
                  <td class="border border-border p-4">
                    <div class="rounded-lg overflow-hidden bg-muted flex items-center justify-center">
                      <img 
                        v-if="category.image" 
                        :src="category.image" 
                        :alt="category.title"
                        class="max-w-full max-h-full object-contain"
                      />
                      <div v-else class="w-full h-full bg-primary/10 flex items-center justify-center">
                        <component :is="category.icon" class="w-8 h-8 text-primary" />
                      </div>
                    </div>
                  </td>
                  <td class="border border-border p-4">
                    <router-link 
                      :to="category.href" 
                      class="font-medium text-lg text-primary hover:text-primary/80 hover:underline transition-colors flex justify-center items-center text-center"
                    >
                      {{ category.title }}
                    </router-link>
                  </td>
                  <td class="border border-border p-1 text-muted-foreground text-center">{{ category.description }}</td>
                  <td class="border border-border p-4">
                    <ul class="space-y-1">
                      <li v-for="feature in category.features" :key="feature" class="flex items-center text-sm">
                        <div class="w-1.5 h-1.5 bg-primary rounded-full mr-2 flex-shrink-0"></div>
                        <span>{{ feature }}</span>
                      </li>
                    </ul>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>


        <!-- CTA Section -->
        <div class="text-center bg-muted/30 rounded-2xl p-12">
          <h2 class="text-3xl font-bold mb-4">Нужна консультация?</h2>
          <p class="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">
            Наши специалисты помогут подобрать оптимальный анализатор для ваших задач
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" class="px-8">
              Получить консультацию
            </Button>
            <Button variant="outline" size="lg" class="px-8">
              Скачать каталог
            </Button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { Button } from "@/components/ui/button";
import { 
  Microscope, 
  TestTube, 
  Activity, 
  Zap, 
  Shield, 
  Target 
} from "lucide-vue-next";

const categories = [
  {
    id: 1,
    title: "СПЕКТРОСКАН MSW",
    description: "Рентгенофлуоресцентный волнодисперсионный анализатор для измерения серы, свинца, марганца и железа",
    icon: Microscope,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОСКАН MSW
    href: "/analyzers/msw",
    features: [
      "Определение серы в нефти и нефтепродуктах",
      "Определение Pb, Fe, Mn в автомобильном бензине",
      "Анализ дистиллятных нефтепродуктов",
      "Высокая точность измерений"
    ]
  },
  {
    id: 2,
    title: "СПЕКТРОСКАН SW-D3",
    description: "Рентгенофлуоресцентный волнодисперсионный анализатор серы для автомобильного топлива",
    icon: TestTube,
    image: "/spectroscan-msw.jpg",// Путь к изображению СПЕКТРОСКАН SW-D3
    href: "/analyzers/sw-d3",
    features: [
      "Арбитражный метод измерения серы",
      "Анализ топлива 3-5 классов",
      "Нефть и нефтепродукты",
      "Соответствие стандартам"
    ]
  },
  {
    id: 3,
    title: "СПЕКТРОСКАН CLSW",
    description: "Рентгенофлуоресцентный волнодисперсионный анализатор для определения хлора и серы",
    icon: Activity,
    image: "/spectroscan-msw.jpg",// Путь к изображению СПЕКТРОСКАН CLSW
    href: "/analyzers/clsw",
    features: [
      "Определение хлорорганических соединений",
      "Анализ содержания серы в топливе",
      "Жидкие пробы",
      "Арбитражные методы"
    ]
  },
  {
    id: 4,
    title: "СПЕКТРОСКАН SE",
    description: "Энергодисперсионный анализатор нового поколения для определения серы",
    icon: Zap,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОСКАН SE
    href: "/analyzers/se",
    features: [
      "Соответствие ГОСТ 32139-2019",
      "Соответствие ISO 20847, ASTM D4294",
      "Быстрое определение серы",
      "Нефть и нефтепродукты"
    ]
  },
  {
    id: 5,
    title: "СПЕКТРОСКАН IS-T",
    description: "Рентгено-абсорбционный поточный анализатор для определения серы в потоке",
    icon: Shield,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОСКАН IS-T
    href: "/analyzers/is-t",
    features: [
      "Непрерывный анализ в потоке",
      "Нефть и нефтепродукты",
      "Высокая производительность",
      "Автоматизация процессов"
    ]
  },
  {
    id: 6,
    title: "СПЕКТРОСКАН МЕТА",
    description: "Элементный анализатор для определения серы и азота методом УФ-флуоресценции",
    icon: Target,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОСКАН МЕТА
    href: "/analyzers/meta",
    features: [
      "УФ-флуоресценция для серы",
      "Хемилюминесценция для азота",
      "Анализ газов и жидкостей",
      "Биологические материалы"
    ]
  }
];


</script>
