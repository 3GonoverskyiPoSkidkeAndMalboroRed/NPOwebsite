<template>
  <div class="bg-white">
    <div class="max-w-4xl mx-auto px-4 py-6">
      <button 
        @click="handleApplication"
        class="bg-gradient-to-r from-green-500 to-green-600 hover:from-green-600 hover:to-green-700 text-white font-semibold py-3 px-8 rounded-lg shadow-lg transition-all duration-200 transform hover:scale-105 focus:outline-none focus:ring-4 focus:ring-green-300"
      >
        {{ buttonText }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  buttonText?: string;
}

const props = withDefaults(defineProps<Props>(), {
  buttonText: 'Отправить заявку'
});

const emit = defineEmits<{
  application: []
}>();

const handleApplication = () => {
  emit('application');
};
</script>

