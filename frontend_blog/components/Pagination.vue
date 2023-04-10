<template>
    <section class="flex items-center h-screen bg-gray-50 dark:bg-gray-900">
        <div class="w-full max-w-screen-xl px-4 mx-auto lg:px-12">
            <!-- Start coding here -->
            <div class="relative overflow-hidden bg-white rounded-b-lg shadow-md dark:bg-gray-800">
                <nav class="flex flex-col items-start justify-between p-4 space-y-3 md:flex-row md:items-center md:space-y-0"
                    aria-label="Table navigation">
                    <span class="text-sm font-normal text-gray-500 dark:text-gray-400">Записей в общем - <span
                            class="font-semibold text-gray-900 dark:text-white"></span><span
                            class="font-semibold text-gray-900 dark:text-white">{{ data.count }}</span></span>
                    <ul class="inline-flex items-stretch -space-x-px">
                        <li>
                            <a :href="`${$route.path}?limit=10&offset=${offset_prev}`"
                                class="flex items-center justify-center h-full py-1.5 px-3 ml-0 text-gray-500 bg-white rounded-l-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                                <span class="sr-only">Previous</span>
                                <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                                        clip-rule="evenodd"></path>
                                </svg>
                            </a>
                        </li>
                        <div v-for="page in range_page">
                            <li>
                                <a :href="`${$route.path}?limit=10&offset=${page * 10}`"
                                    class="flex items-center justify-center px-3 py-2 text-sm leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                                    {{ page + 1 }}</a>
                            </li>
                        </div>
                        <li>
                            <a :href="`${$route.path}?limit=10&offset=${offset_next}`"
                                class="flex items-center justify-center h-full py-1.5 px-3 leading-tight text-gray-500 bg-white rounded-r-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                                <span class="sr-only">Next</span>
                                <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                        clip-rule="evenodd"></path>
                                </svg>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </section>
</template>

<script setup>

const { data } = defineProps(['data'])
const count_page = Math.ceil(data.count / 10)
const { offset } = useRoute().query
const range = n => {
    let result = []
    for (let i = 0; i < n; i += 1) {
        result.push(i)
    }
    return result
}

let offset_next = offset
let offset_prev = 0

if (data.next) {
    offset_next = new URL(data.next).searchParams.get('offset')

} if (data.previous) {
    offset_prev = new URL(data.previous).searchParams.get('offset')
}

const range_page = range(count_page)

</script>


