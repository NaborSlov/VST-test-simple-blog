<template>
    <section class="bg-white dark:bg-gray-900">
        <div class="py-8 px-4 mx-auto max-w-2xl lg:py-16">
            <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">Новый блог</h2>
            <form @submit.prevent="createBlog">
                <div class="grid gap-4 sm:grid-cols-1 sm:gap-6">
                    <div class="sm:col-span-2">
                        <label for="title"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Название</label>
                        <input type="text" name="title" id="title" v-model="title"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Название твоего блога" required="">
                    </div>
                    <div class="w-full">
                        <label for="theme" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Тема</label>
                        <input type="text" name="theme" id="theme" v-model="theme"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Тема твоего блога" required="">
                    </div>
                    <div class="sm:col-span-2">
                        <label for="description"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Описание</label>
                        <textarea id="description" rows="8" v-model="description"
                            class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Описание твоего блога"></textarea>
                    </div>
                </div>
                <button type="submit"
                    class="inline-flex items-center px-5 py-2.5 mt-4 sm:mt-6 text-sm font-medium text-center text-white bg-primary-700 rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
                    Создать блог
                </button>
            </form>
        </div>
    </section>
</template>

<script setup>

const title = ref('')
const theme = ref('')
const description = ref('')

const cookie = useCookie('sessionid').value
const csrf_token = useCookie('csrftoken').value

async function createBlog() {
    const response = await $fetch('/api/blogs/createBlog', {
        method: 'post',
        body: {
            title: title.value,
            theme: theme.value,
            description: description.value,
            cookie: cookie,
            csrf_token: csrf_token
        }
    })

    if (response.auth === false) {
        navigateTo('/auth/')
    } if (response.error) {
        createError()  // Написать страницу ошибок
    }

    navigateTo('/')

}

</script>

<style scoped></style>