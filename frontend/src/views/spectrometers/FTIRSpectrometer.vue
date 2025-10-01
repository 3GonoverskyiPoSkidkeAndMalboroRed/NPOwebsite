<template>
  <DevicePageLayout>
    <!-- Hero Section -->
    <DeviceHero
      title="СПЕКТРОМЕТР ИК-Фурье"
      description="Инфракрасный спектрометр Фурье для молекулярного анализа и идентификации соединений"
      :main-image="mainImage"
      :images="[mainImage]"
      @open-image-modal="() => {}"
    />

    <!-- Tabs Section -->
    <DeviceTabs
      :active-tab="activeTab"
      :tabs="tabs"
      @update:active-tab="activeTab = $event"
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


  </DevicePageLayout>
</template>

<script setup lang="ts">
import { ref } from "vue";
import DeviceHero from "@/components/device/DeviceHero.vue";
import DeviceTabs from "@/components/device/DeviceTabs.vue";
import DeviceDescription from "@/components/device/DeviceDescription.vue";
import DeviceSpecifications from "@/components/device/DeviceSpecifications.vue";
import DeviceAdvantages from "@/components/device/DeviceAdvantages.vue";
import DeviceTasks from "@/components/device/DeviceTasks.vue";
import DevicePageLayout from "@/components/device/DevicePageLayout.vue";

// Управление вкладками
const activeTab = ref('description');

// Главное изображение
const mainImage = '/spectroscan-msw.jpg';

const tabs = [
  { id: 'description', label: 'Описание' },
  { id: 'specifications', label: 'Характеристики' },
  { id: 'advantages', label: 'Преимущества' },
  { id: 'tasks', label: 'Задачи' }
];

// Данные для описания
const description = [
  "СПЕКТРОМЕТР ИК-Фурье — высокоточный прибор для молекулярного анализа органических и неорганических соединений. Прибор использует технологию преобразования Фурье для получения высококачественных инфракрасных спектров.",
  "Анализатор обеспечивает быструю идентификацию соединений, контроль качества материалов и структурный анализ молекул. Широкий спектральный диапазон позволяет анализировать различные типы образцов.",
  "Современное программное обеспечение включает обширные библиотеки спектров для автоматической идентификации соединений и количественного анализа."
];

// Данные для характеристик
const analyticalParams = {
  left: [
    { label: "Спектральный диапазон", value: "4000-400 см⁻¹" },
    { label: "Разрешение", value: "0,25 см⁻¹" },
    { label: "Точность волновых чисел", value: "±0,01 см⁻¹" }
  ],
  right: [
    { label: "Время сканирования", value: "1-30 секунд" },
    { label: "Соотношение сигнал/шум", value: "50000:1" },
    { label: "Точность пропускания", value: "±0,1%" }
  ]
};

const technicalParams = {
  left: [
    { label: "Тип прибора", value: "ИК-Фурье спектрометр" },
    { label: "Источник излучения", value: "Глобар" },
    { label: "Детектор", value: "DTGS" }
  ],
  right: [
    { label: "Интерферометр", value: "Мишельсона" },
    { label: "Программное обеспечение", value: "Spectrum One" },
    { label: "Габариты", value: "600×500×300 мм" }
  ]
};

// Данные для преимуществ
const advantages = [
  "высокое разрешение и точность;",
  "быстрое сканирование;",
  "широкий спектральный диапазон;",
  "автоматическая идентификация;",
  "обширные библиотеки спектров;",
  "простота эксплуатации."
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
