// Утилита для автоматического рефакторинга страниц устройств
export const refactorDevicePage = (pageContent: string, deviceType: 'analyzer' | 'spectrometer'): string => {
  // Базовые импорты для всех страниц
  const baseImports = `import { ref, onMounted, onUnmounted } from "vue";
import DeviceHero from "@/components/DeviceHero.vue";
import DeviceTabs from "@/components/DeviceTabs.vue";
import DeviceDescription from "@/components/DeviceDescription.vue";
import DeviceSpecifications from "@/components/DeviceSpecifications.vue";
import DeviceAdvantages from "@/components/DeviceAdvantages.vue";
import DeviceDocumentation from "@/components/DeviceDocumentation.vue";
import DeviceTasks from "@/components/DeviceTasks.vue";
import DeviceMaterials from "@/components/DeviceMaterials.vue";
import DeviceCTA from "@/components/DeviceCTA.vue";
import DeviceImageModal from "@/components/DeviceImageModal.vue";`;

  // Шаблон для CTA секции
  const ctaTitle = deviceType === 'analyzer' ? 'Заинтересовал анализатор?' : 'Заинтересовал спектрометр?';
  
  // Заменяем template
  const newTemplate = `<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <DeviceHero
      title="DEVICE_TITLE"
      description="DEVICE_DESCRIPTION"
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

        <!-- Документация -->
        <DeviceDocumentation
          :active-tab="activeTab"
          :documentation="documentation"
        />

        <!-- Решаемые задачи -->
        <DeviceTasks
          :active-tab="activeTab"
          :tasks="tasks"
        />

        <!-- Материалы -->
        <DeviceMaterials
          :active-tab="activeTab"
          :materials="materials"
        />
      </template>
    </DeviceTabs>

    <!-- CTA Section -->
    <DeviceCTA
      title="${ctaTitle}"
      description="Получите подробную консультацию и техническое предложение от наших специалистов"
    />

    <!-- Модальное окно для просмотра изображений -->
    <DeviceImageModal
      :is-open="isModalOpen"
      :images="images"
      device-name="DEVICE_NAME"
      :current-index="currentImageIndex"
      @close="closeImageModal"
      @update:current-index="currentImageIndex = $event"
    />
  </div>
</template>`;

  // Базовый script setup
  const baseScript = `${baseImports}

// Управление вкладками
const activeTab = ref('description');

// Управление модальным окном изображений
const isModalOpen = ref(false);
const currentImageIndex = ref(0);

// Массив изображений
const images = [
  'IMAGE_PATH'
];

// Функции для работы с модальным окном
const openImageModal = (index: number) => {
  currentImageIndex.value = index;
  isModalOpen.value = true;
};

const closeImageModal = () => {
  isModalOpen.value = false;
};

// Обработка клавиатурных событий
const handleKeydown = (event: KeyboardEvent) => {
  if (!isModalOpen.value) return;
  
  switch (event.key) {
    case 'Escape':
      closeImageModal();
      break;
  }
};

onMounted(() => {
  document.addEventListener('keydown', handleKeydown);
});

onUnmounted(() => {
  document.removeEventListener('keydown', handleKeydown);
});

const tabs = [
  { id: 'description', label: 'Описание' },
  { id: 'specifications', label: 'Характеристики' },
  { id: 'advantages', label: 'Преимущества' },
  { id: 'documentation', label: 'Документация' },
  { id: 'tasks', label: 'Задачи' },
  { id: 'materials', label: 'Материалы' }
];

// Данные для страницы (заполняются вручную)
const description = [];
const analyticalParams = { left: [], right: [] };
const technicalParams = { left: [], right: [] };
const advantages = [];
const documentation = [];
const tasks = [];
const materials = [];`;

  return newTemplate + '\n\n<script setup lang="ts">\n' + baseScript + '\n</script>';
};
