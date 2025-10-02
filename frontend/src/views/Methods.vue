<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <section class="py-20 px-4 bg-gradient-to-b from-background to-muted/20">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text">
            Методики
          </h1>
        </div>

        <!-- Детальная страница методики -->
        <div v-if="showMethodDetail && selectedMethod" class="bg-white rounded-lg shadow-lg overflow-hidden">
          <div class="px-4 py-4 border-b border-gray-200">
            <button 
              @click="showMethodDetail = false"
              class="flex items-center gap-2 text-gray-600 hover:text-gray-800 transition-colors"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
              </svg>
              Назад к списку методик
            </button>
          </div>
          <MethodHeader :title="selectedMethod.title" />
          
          <MethodDescription 
            :standards-description="selectedMethod.standards_description || ''"
            :method-description="selectedMethod.method_description || ''"
          />
          
          <ApplicationButton @application="handleApplication" />
          
          <MethodTabs 
            :tabs="tabs"
            :active-tab="activeTab"
            @tab-change="handleTabChange"
          />
          
          <MethodContent 
            :active-tab="activeTab"
            :description-content="selectedMethod.description_content"
            :limitations="selectedMethod.limitations"
            :procedure="selectedMethod.procedure"
            :documentation="selectedMethod.documentation"
            :equipment="selectedMethod.equipment"
          />
          
          <MethodFooter />
        </div>

        <!-- Список методик по отраслям -->
        <div v-else class="space-y-12">
          <!-- Индикатор загрузки -->
          <div v-if="loading" class="text-center py-8">
            <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
            <p class="mt-2 text-gray-600">Загрузка методик...</p>
          </div>
          
          <!-- Ошибка загрузки -->
          <div v-else-if="error" class="text-center py-8">
            <p class="text-red-600">Ошибка загрузки: {{ error }}</p>
            <button 
              @click="fetchMethods()" 
              class="mt-2 px-4 py-2 bg-primary text-white rounded hover:bg-primary/80"
            >
              Попробовать снова
            </button>
          </div>
          
          <!-- Список методик -->
          <div v-else-if="methodBlocks.length > 0">
            <MethodBlock
              v-for="method in methodBlocks"
              :key="method.title"
              :method="method"
              @method-select="handleMethodSelect"
            />
          </div>
          
          <!-- Пустое состояние -->
          <div v-else class="text-center py-8">
            <p class="text-gray-600">Методики не найдены</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import MethodBlock from "@/components/MethodBlock.vue";
import MethodHeader from "@/components/method/MethodHeader.vue";
import MethodDescription from "@/components/method/MethodDescription.vue";
import ApplicationButton from "@/components/method/ApplicationButton.vue";
import MethodTabs from "@/components/method/MethodTabs.vue";
import MethodContent from "@/components/method/MethodContent.vue";
import MethodFooter from "@/components/method/MethodFooter.vue";
import { useMethods, type Method } from "@/composables/useMethods";


// Используем composable для работы с методиками
const { methods, loading, error, methodBlocks, fetchMethods, fetchMethodById } = useMethods();

// Состояние для переключения между списком и детальной страницей
const showMethodDetail = ref(false);
const activeTab = ref('range');
const selectedMethod = ref<Method | null>(null);

// Вкладки
const tabs = [
  { id: 'description', label: 'Описание методики' },
  { id: 'range', label: 'Диапазон измерений' },
  { id: 'documentation', label: 'Документация' },
  { id: 'equipment', label: 'Доп. оборудование' }
];

// Получаем route для обработки параметров
const route = useRoute();

// Обработчики событий
const handleMethodSelect = async (methodId?: number) => {
  if (methodId) {
    const method = await fetchMethodById(methodId);
    if (method) {
      selectedMethod.value = method as Method;
      showMethodDetail.value = true;
    }
  } else {
    // Для демонстрации загружаем первую доступную методику
    if (methods.value.length > 0) {
      selectedMethod.value = methods.value[0] as Method;
      showMethodDetail.value = true;
    }
  }
};

const handleTabChange = (tabId: string) => {
  activeTab.value = tabId;
};

const handleApplication = () => {
  // Логика отправки заявки
  console.log('Отправка заявки');
};

// Загрузка данных при монтировании компонента
onMounted(async () => {
  await fetchMethods();
  
  // Проверяем, есть ли ID методики в URL
  const methodId = route.params.id;
  if (methodId && typeof methodId === 'string') {
    const id = parseInt(methodId);
    if (!isNaN(id)) {
      await handleMethodSelect(id);
    }
  }
});

</script>
