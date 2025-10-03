<template>
  <div 
    v-if="isOpen" 
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm"
    @click="close"
  >
    <div class="relative max-w-7xl max-h-[90vh] w-full mx-4">
      <!-- Кнопка закрытия -->
      <button 
        @click.stop="close"
        class="absolute top-4 right-4 z-10 bg-black/50 text-white rounded-full p-2 hover:bg-black/70 transition-colors"
      >
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>

      <!-- Кнопка "Назад" -->
      <button 
        v-if="images.length > 1"
        @click.stop="previous"
        class="absolute left-4 top-1/2 -translate-y-1/2 z-10 bg-black/50 text-white rounded-full p-3 hover:bg-black/70 transition-colors"
      >
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
        </svg>
      </button>

      <!-- Кнопка "Вперед" -->
      <button 
        v-if="images.length > 1"
        @click.stop="next"
        class="absolute right-4 top-1/2 -translate-y-1/2 z-10 bg-black/50 text-white rounded-full p-3 hover:bg-black/70 transition-colors"
      >
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
        </svg>
      </button>

      <!-- Изображение -->
      <img 
        :src="images[currentIndex]" 
        :alt="`${deviceName} - изображение ${currentIndex + 1}`"
        class="w-full h-full rounded-lg"
        :class="imageClass"
        @click.stop
        @load="onImageLoad"
        ref="currentImage"
      />

      <!-- Индикатор текущего изображения -->
      <div v-if="images.length > 1" class="absolute bottom-4 left-1/2 -translate-x-1/2 bg-black/50 text-white px-3 py-1 rounded-full text-sm">
        {{ currentIndex + 1 }} / {{ images.length }}
      </div>

      <!-- Миниатюры в модальном окне -->
      <div v-if="images.length > 1" class="absolute bottom-16 left-1/2 -translate-x-1/2 flex gap-2">
        <button 
          v-for="(image, index) in images" 
          :key="index"
          @click.stop="currentIndex = index"
          class="w-12 h-12 rounded overflow-hidden border-2 transition-all"
          :class="currentIndex === index ? 'border-white' : 'border-white/50 hover:border-white/80'"
        >
          <img 
            :src="image" 
            :alt="`Миниатюра ${index + 1}`"
            class="w-full h-full object-cover"
          />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from "vue";

interface Props {
  isOpen: boolean;
  images: string[];
  deviceName: string;
  currentIndex: number;
}

const props = defineProps<Props>();

const emit = defineEmits<{
  close: [];
  'update:currentIndex': [index: number];
}>();

const currentIndex = ref(props.currentIndex);
const currentImage = ref<HTMLImageElement | null>(null);
const isVertical = ref(false);

watch(() => props.currentIndex, (newIndex) => {
  currentIndex.value = newIndex;
});

// Computed свойство для CSS класса изображения
const imageClass = computed(() => {
  return isVertical.value 
    ? 'object-contain max-h-[90vh] mx-auto' 
    : 'object-contain';
});

// Функция для определения ориентации изображения
const onImageLoad = () => {
  if (currentImage.value) {
    const img = currentImage.value;
    isVertical.value = img.naturalHeight > img.naturalWidth;
  }
};

const close = () => {
  emit('close');
};

const next = () => {
  if (currentIndex.value < props.images.length - 1) {
    currentIndex.value++;
  } else {
    currentIndex.value = 0; // Циклический переход к первому изображению
  }
  emit('update:currentIndex', currentIndex.value);
};

const previous = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--;
  } else {
    currentIndex.value = props.images.length - 1; // Циклический переход к последнему изображению
  }
  emit('update:currentIndex', currentIndex.value);
};
</script>
