<script setup lang="ts">
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";

interface FAQProps {
  question: string;
  answer: string;
  value: string;
}

const faqList: FAQProps[] = [
  {
    question: "Какие приборы производит НПО «СПЕКТРОН»?",
    answer: "НПО «СПЕКТРОН» производит спектрометры и анализаторы серии СПЕКТРОСКАН для рентгеновского флуоресцентного анализа, анализаторы серы, хлора, азота, а также вакуумные волнодисперсионные рентгенофлуоресцентные спектрометры.",
    value: "item-1",
  },
  {
    question: "Где можно купить оборудование СПЕКТРОСКАН?",
    answer: "Оборудование можно приобрести через официальных дилеров НПО «СПЕКТРОН» или обратившись напрямую в отдел продаж по телефону (812) 325-8183 или электронной почте rus@spectronxray.ru.",
    value: "item-2",
  },
  {
    question: "Предоставляется ли техническая поддержка?",
    answer: "Да, НПО «СПЕКТРОН» предоставляет полный спектр технической поддержки: установка и настройка оборудования, обучение персонала, гарантийное и постгарантийное обслуживание, разработка методик анализа.",
    value: "item-3",
  },
  {
    question: "Есть ли сервисные центры в регионах?",
    answer: "Да, у нас есть сеть сервисных центров по всей России, которые обеспечивают своевременное техническое обслуживание и ремонт оборудования СПЕКТРОСКАН.",
    value: "item-4",
  },
  {
    question: "Какие методики анализа аттестованы?",
    answer: "У нас аттестовано свыше 50 методик анализа для различных областей: анализ почв, углей, водных сред АЭС, металлов и сплавов. Все методики соответствуют российским стандартам и имеют соответствующие сертификаты.",
    value: "item-5",
  },
];
</script>

<template>
  <section
    id="faq"
    class="container px-4 sm:px-6 lg:px-8 py-16 sm:py-20 md:py-24 lg:py-32"
  >
    <div class="max-w-4xl mx-auto">
      <div class="text-center mb-8 sm:mb-12">
        <h2 class="text-2xl sm:text-3xl md:text-4xl font-bold mb-4">
          Часто задаваемые вопросы
        </h2>
        <p class="text-muted-foreground text-sm sm:text-base">
          Ответы на популярные вопросы о нашей продукции и услугах
        </p>
      </div>

      <Accordion
        type="single"
        collapsible
        class="AccordionRoot space-y-2"
      >
        <AccordionItem
          v-for="{ question, answer, value } in faqList"
          :key="value"
          :value="value"
          class="border rounded-lg px-4 sm:px-6"
        >
          <AccordionTrigger class="text-left text-sm sm:text-base py-4 sm:py-6">
            {{ question }}
          </AccordionTrigger>

          <AccordionContent class="text-sm sm:text-base text-muted-foreground pb-4 sm:pb-6">
            {{ answer }}
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      <div class="text-center mt-8 sm:mt-12">
        <h3 class="font-medium text-sm sm:text-base mb-2">
          Остались вопросы?
        </h3>
        <a
          href="tel:+78123258183"
          class="text-primary hover:text-primary/80 underline text-sm sm:text-base"
        >
          Свяжитесь с нами
        </a>
      </div>
    </div>
  </section>
</template>
