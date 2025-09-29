<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <section class="py-20 px-4 bg-gradient-to-b from-background to-muted/20">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text">
            Горнорудная промышленность
          </h1>
   
        </div>

        <!-- Методики -->
        <div class="space-y-8">
          <div class="p-8">
            <div class="space-y-6">
              <div 
                v-for="method in methods" 
                :key="method.title"
                class="flex gap-4 items-center"
              >
                <div class="flex-shrink-0">
                  <img 
                    :src="method.image"
                    :alt="method.title"
                    class="w-10 h-10 rounded-lg object-cover"
                  />
                </div>
                <div class="flex-1">
                  <h3 class="font-semibold text-lg mb-2">{{ method.title }}</h3>
                  <p class="text-muted-foreground">{{ method.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
interface Method {
  title: string;
  image: string;
  description: string;
}

const methods: Method[] = [
  {
    title: "Анализ коррозионных отложений",
    image: "/лого-методик/Диагностика и контроль/Анализ коррозионных отложений.png",
    description: "Комплексная методика анализа природных, питьевых и сточных вод для определения их химического состава, содержания загрязнителей и соответствия санитарно-гигиеническим нормативам."
  },
  {
    title: "Анализ продуктов износа в консистентных смазках",
    image: "/лого-методик/Диагностика и контроль/Анализ продуктов износа в консистентных смазках.png",
    description: "Методика определения элементного состава растительных материалов и продуктов питания для оценки их качества, безопасности и пищевой ценности."
  },
  {
    title: "Анализ технологических водных сред АЭС",
    image: "/лого-методик/Диагностика и контроль/Анализ технологических водных сред АЭС.png",
    description: "Методика анализа воздуха рабочей зоны и вентиляционных выбросов для контроля соблюдения гигиенических нормативов и обеспечения безопасности труда."
  },
  {
    title: "Диагностика износа двигателей",
    image: "/лого-методик/Диагностика и контроль/Диагностика износа двигателей.png",
    description: "Методика анализа отходов минерального происхождения для определения их состава, токсичности и возможности дальнейшего использования или утилизации."
  },

];
</script>

