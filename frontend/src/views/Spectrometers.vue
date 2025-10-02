<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <section class="py-20 px-4">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text ">
            Спектрометры
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


     
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
// import { Button } from "@/components/ui/button";
import { 
  Microscope, 
  TestTube, 
  Activity, 
  Zap, 
  Shield, 
  Target,
  Atom,
  Waves,
  ScanLine
} from "lucide-vue-next";

const categories = [
  {
    id: 1,
    title: "СПЕКТРОМЕТР ИСП-МС",
    description: "ИСП-масс-спектрометр для элементного анализа с индуктивно связанной плазмой",
    icon: Microscope,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОМЕТР ИСП-МС
    href: "/spectrometers/icp-ms",
    features: [
      "Определение следовых элементов",
      "Анализ металлов и сплавов",
      "Экологические исследования",
      "Высокая чувствительность"
    ]
  },
  {
    id: 2,
    title: "СПЕКТРОМЕТР ИСП-ОЭС",
    description: "ИСП-оптико-эмиссионный спектрометр для анализа металлов и сплавов",
    icon: TestTube,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОМЕТР ИСП-ОЭС
    href: "/spectrometers/icp-oes",
    features: [
      "Анализ металлов и сплавов",
      "Определение примесей",
      "Быстрый анализ",
      "Широкий диапазон элементов"
    ]
  },
  {
    id: 3,
    title: "СПЕКТРОМЕТР ААС",
    description: "Атомно-абсорбционный спектрометр для определения металлов",
    icon: Activity,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОМЕТР ААС
    href: "/spectrometers/aas",
    features: [
      "Определение тяжелых металлов",
      "Анализ воды и почвы",
      "Высокая точность",
      "Простота использования"
    ]
  },
  {
    id: 4,
    title: "СПЕКТРОМЕТР ИК-Фурье",
    description: "Инфракрасный спектрометр Фурье для молекулярного анализа",
    icon: Zap,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОМЕТР ИК-Фурье
    href: "/spectrometers/ftir",
    features: [
      "Идентификация органических соединений",
      "Контроль качества",
      "Анализ полимеров",
      "Быстрое сканирование"
    ]
  },
  {
    id: 5,
    title: "СПЕКТРОМЕТР УФ-Видимый",
    description: "Ультрафиолетово-видимый спектрометр для анализа органических соединений",
    icon: Shield,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОМЕТР УФ-Видимый
    href: "/spectrometers/uv-vis",
    features: [
      "Анализ органических соединений",
      "Определение концентраций",
      "Кинетические исследования",
      "Широкий спектральный диапазон"
    ]
  },
  {
    id: 6,
    title: "СПЕКТРОМЕТР ЯМР",
    description: "Ядерно-магнитный резонансный спектрометр для структурного анализа",
    icon: Target,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОМЕТР ЯМР
    href: "/spectrometers/nmr",
    features: [
      "Структурный анализ молекул",
      "Идентификация соединений",
      "Количественный анализ",
      "Исследования в химии"
    ]
  },
  {
    id: 7,
    title: "СПЕКТРОМЕТР МС",
    description: "Масс-спектрометр для анализа органических и неорганических соединений",
    icon: Atom,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОМЕТР МС
    href: "/spectrometers/ms",
    features: [
      "Анализ органических соединений",
      "Определение молекулярной массы",
      "Структурная идентификация",
      "Высокая чувствительность"
    ]
  },
  {
    id: 8,
    title: "СПЕКТРОМЕТР Рамановский",
    description: "Рамановский спектрометр для молекулярного анализа и идентификации",
    icon: Waves,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОМЕТР Рамановский
    href: "/spectrometers/raman",
    features: [
      "Идентификация материалов",
      "Анализ кристаллических структур",
      "Неразрушающий контроль",
      "Быстрый анализ"
    ]
  },
  {
    id: 9,
    title: "СПЕКТРОМЕТР РСА",
    description: "Рентгеноструктурный анализатор для кристаллографических исследований",
    icon: ScanLine,
    image: "/spectroscan-msw.jpg", // Путь к изображению СПЕКТРОМЕТР РСА
    href: "/spectrometers/xrd",
    features: [
      "Анализ кристаллических структур",
      "Фазовый анализ",
      "Исследование материалов",
      "Определение размеров кристаллов"
    ]
  }
];


</script>
