import { ref, computed } from 'vue'

export function useInputMasks() {
  // Маска для ФИО - только буквы, пробелы и дефисы
  const fullNameMask = ref('')
  
  // Маска для телефона - российский формат
  const phoneMask = ref('')
  
  // Функция для валидации ФИО
  const validateFullName = (value: string): boolean => {
    // Проверяем, что содержит только буквы, пробелы и дефисы
    const regex = /^[а-яёА-ЯЁ\s\-]+$/i
    return regex.test(value)
  }
  
  // Функция для валидации телефона
  const validatePhone = (value: string): boolean => {
    // Убираем все нецифровые символы
    const digits = value.replace(/\D/g, '')
    // Проверяем, что номер начинается с 7 или 8 и имеет 11 цифр
    return (digits.startsWith('7') || digits.startsWith('8')) && digits.length === 11
  }
  
  // Функция форматирования телефона
  const formatPhone = (value: string): string => {
    // Убираем все нецифровые символы
    const digits = value.replace(/\D/g, '')
    
    // Если номер начинается с 8, заменяем на 7
    let cleanDigits = digits
    if (cleanDigits.startsWith('8')) {
      cleanDigits = '7' + cleanDigits.slice(1)
    }
    
    // Если номер начинается с 7 и имеет 11 цифр
    if (cleanDigits.startsWith('7') && cleanDigits.length === 11) {
      return `+7 (${cleanDigits.slice(1, 4)}) ${cleanDigits.slice(4, 7)}-${cleanDigits.slice(7, 9)}-${cleanDigits.slice(9, 11)}`
    }
    
    // Если номер начинается с 7 и имеет меньше 11 цифр
    if (cleanDigits.startsWith('7')) {
      const formatted = cleanDigits.slice(1)
      if (formatted.length <= 3) {
        return `+7 (${formatted}`
      } else if (formatted.length <= 6) {
        return `+7 (${formatted.slice(0, 3)}) ${formatted.slice(3)}`
      } else if (formatted.length <= 8) {
        return `+7 (${formatted.slice(0, 3)}) ${formatted.slice(3, 6)}-${formatted.slice(6)}`
      } else {
        return `+7 (${formatted.slice(0, 3)}) ${formatted.slice(3, 6)}-${formatted.slice(6, 8)}-${formatted.slice(8)}`
      }
    }
    
    // Если номер не начинается с 7 или 8
    if (cleanDigits.length > 0) {
      return `+7 (${cleanDigits.slice(0, 3)}`
    }
    
    return ''
  }
  
  // Функция для обработки ввода ФИО
  const handleFullNameInput = (event: Event) => {
    const target = event.target as HTMLInputElement
    let value = target.value
    
    // Убираем все символы, кроме букв, пробелов и дефисов
    value = value.replace(/[^а-яёА-ЯЁ\s\-]/gi, '')
    
    // Убираем множественные пробелы
    value = value.replace(/\s+/g, ' ')
    
    // Убираем пробелы в начале и конце
    value = value.trim()
    
    target.value = value
    fullNameMask.value = value
  }
  
  // Функция для обработки ввода телефона
  const handlePhoneInput = (event: Event) => {
    const target = event.target as HTMLInputElement
    let value = target.value
    
    // Убираем все нецифровые символы
    const digits = value.replace(/\D/g, '')
    
    // Если пользователь начал вводить с 8, заменяем на 7
    let cleanDigits = digits
    if (cleanDigits.startsWith('8')) {
      cleanDigits = '7' + cleanDigits.slice(1)
    }
    
    // Ограничиваем до 11 цифр
    if (cleanDigits.length > 11) {
      cleanDigits = cleanDigits.slice(0, 11)
    }
    
    // Форматируем номер
    const formatted = formatPhone(cleanDigits)
    target.value = formatted
    phoneMask.value = formatted
  }
  
  // Функция для обработки вставки телефона
  const handlePhonePaste = (event: ClipboardEvent) => {
    event.preventDefault()
    const pastedText = event.clipboardData?.getData('text') || ''
    
    // Убираем все нецифровые символы
    const digits = pastedText.replace(/\D/g, '')
    
    // Если номер начинается с 8, заменяем на 7
    let cleanDigits = digits
    if (cleanDigits.startsWith('8')) {
      cleanDigits = '7' + cleanDigits.slice(1)
    }
    
    // Ограничиваем до 11 цифр
    if (cleanDigits.length > 11) {
      cleanDigits = cleanDigits.slice(0, 11)
    }
    
    // Форматируем и устанавливаем значение
    const formatted = formatPhone(cleanDigits)
    const target = event.target as HTMLInputElement
    target.value = formatted
    phoneMask.value = formatted
  }
  
  // Вычисляемые свойства для валидации
  const isFullNameValid = computed(() => {
    return fullNameMask.value.length > 0 && validateFullName(fullNameMask.value)
  })
  
  const isPhoneValid = computed(() => {
    return phoneMask.value.length > 0 && validatePhone(phoneMask.value)
  })
  
  return {
    fullNameMask,
    phoneMask,
    validateFullName,
    validatePhone,
    formatPhone,
    handleFullNameInput,
    handlePhoneInput,
    handlePhonePaste,
    isFullNameValid,
    isPhoneValid
  }
}
