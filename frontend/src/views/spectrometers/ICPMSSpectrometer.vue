<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <DeviceHero
      title="СПЕКТРОМЕТР ИСП-МС"
      description="ИСП-масс-спектрометр для элементного анализа с индуктивно связанной плазмой"
      :main-image="images[0]"
      :images="images"
      @open-image-modal="openImageModal"
    />

    <!-- Tabs Section -->
    <DeviceTabs
      v-model:active-tab="activeTab"
      :tabs="tabs"
    >
      <template #default="{ activeTab }">
        <!-- Описание -->
        <DeviceDescription
          :active-tab="activeTab"
          :description="description"
        />

        <!-- Характеристики -->
        <DeviceSpecifications
          :active-tab="activeTab"
          :analytical-params="analyticalParams"
          :technical-params="technicalParams"
        />

        <!-- Преимущества -->
        <DeviceAdvantages
          :active-tab="activeTab"
          :advantages="advantages"
        />

        <!-- Решаемые задачи -->
        <DeviceTasks
          :active-tab="activeTab"
          :tasks="tasks"
        />
      </template>
    </DeviceTabs>

    <!-- CTA Section -->
    <DeviceCTA
      title="Заинтересовал спектрометр?"
      description="Получите подробную консультацию и техническое предложение от наших специалистов"
    />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import DeviceHero from "@/components/device/DeviceHero.vue";
import DeviceTabs from "@/components/device/DeviceTabs.vue";
import DeviceDescription from "@/components/device/DeviceDescription.vue";
import DeviceSpecifications from "@/components/device/DeviceSpecifications.vue";
import DeviceAdvantages from "@/components/device/DeviceAdvantages.vue";
import DeviceTasks from "@/components/device/DeviceTasks.vue";
import DeviceCTA from "@/components/device/DeviceCTA.vue";

// Управление вкладками
const activeTab = ref('description');

// Массив изображений
const images = [
  '/spectroscan-msw.jpg'
];

// Функция для открытия модального окна (заглушка)
const openImageModal = (index: number) => {
  // Для спектрометров пока не реализовано модальное окно
  console.log('Open image modal:', index);
};

const tabs = [
  { id: 'description', label: 'Описание' },
  { id: 'specifications', label: 'Характеристики' },
  { id: 'advantages', label: 'Преимущества' },
  { id: 'tasks', label: 'Задачи' }
];

// Описание
const description = [
  "СПЕКТРОМЕТР ИСП-МС — высокочувствительный прибор для элементного анализа с использованием индуктивно связанной плазмы и масс-спектрометрии. Прибор предназначен для определения следовых элементов в широком диапазоне концентраций.",
  "Анализатор обеспечивает превосходную чувствительность и селективность для определения металлов и неметаллов в различных типах проб: вода, почва, биологические материалы, металлы и сплавы.",
  "Технология ИСП-МС позволяет проводить одновременное определение более 70 элементов периодической системы с пределами обнаружения на уровне пикограмм на литр."
];

// Аналитические параметры
const analyticalParams = {
  left: [
    { label: "Определяемые элементы", value: "70+ элементов" },
    { label: "Диапазон масс", value: "3-300 а.е.м." },
    { label: "Чувствительность", value: "пг/л" }
  ],
  right: [
    { label: "Время анализа", value: "1-3 минуты" },
    { label: "Линейный диапазон", value: "6-8 порядков" },
    { label: "Точность", value: "±2-5%" }
  ]
};

// Технические параметры
const technicalParams = {
  left: [
    { label: "Тип прибора", value: "ИСП-масс-спектрометр" },
    { label: "Частота ИСП", value: "27,12 МГц" },
    { label: "Мощность ИСП", value: "1,0-1,5 кВт" }
  ],
  right: [
    { label: "Тип детектора", value: "Электронный умножитель" },
    { label: "Разрешение", value: "0,7 а.е.м." },
    { label: "Габариты", value: "1200×800×1800 мм" }
  ]
};

// Преимущества
const advantages = [
  "высокая чувствительность (пг/л);",
  "широкий линейный диапазон;",
  "одновременное определение множества элементов;",
  "высокая селективность;",
  "автоматическая калибровка;",
  "простота эксплуатации."
];

// Данные для решаемых задач
const tasks = [
  {
    title: "Анализ следовых элементов",
    description: "Определение ультранизких концентраций металлов в воде, почве и биологических материалах",
    application: "Экологические лаборатории, токсикологические центры"
  },
  {
    title: "Контроль качества металлов",
    description: "Анализ чистоты металлов и сплавов на содержание примесей",
    application: "Металлургические предприятия, сертификационные центры"
  },
  {
    title: "Медицинские исследования",
    description: "Определение микроэлементов в биологических жидкостях и тканях",
    application: "Медицинские лаборатории, исследовательские центры"
  }
];
</script>
