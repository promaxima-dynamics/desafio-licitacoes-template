import { defineStore } from 'pinia'
import { ref } from 'vue'
// import axios from 'axios' // Ou use fetch

export const useMyStore = defineStore('myStore', () => {
  // State
  const items = ref([])
  const stats = ref({})
  const loading = ref(false)
  const error = ref(null)

  // Getters (computed)
  // const totalItems = computed(() => items.value.length)

  // Actions
  async function fetchItems(searchTerm = '') {
    loading.value = true
    error.value = null
    try {
      // TODO: Ajuste a URL da API e parâmetros
      // const response = await axios.get(`/api/items/?search=${searchTerm}`)
      // items.value = response.data.results // Assumindo paginação DRF
      console.log('Placeholder fetchItems na store', searchTerm)
      // Fetch stats as well
      // const statsResponse = await axios.get(`/api/items/stats/?search=${searchTerm}`)
      // stats.value = statsResponse.data
    } catch (err) {
      error.value = 'Falha ao buscar itens.'
      console.error(err)
    } finally {
      loading.value = false
    }
  }

  async function exportItems(selectedIds) {
    // TODO: Implementar lógica para chamar endpoint de exportação ou gerar XLS no frontend
    console.log('Placeholder exportItems na store', selectedIds)
    alert('Funcionalidade de exportar não implementada.')
  }

  return { items, stats, loading, error, fetchItems, exportItems }
}) 