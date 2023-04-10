<template>
    <section class="bg-white dark:bg-gray-900">
        <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
            <div class="mx-auto max-w-screen-sm text-center lg:mb-16 mb-8">
                <h2 class="mb-4 text-3xl lg:text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Главная
                    страница
                </h2>
                <NuxtLink to="/blogs/create">
                    <button
                        class="text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800">
                        Создать блог</button>
                </NuxtLink>
            </div>
            <div class="grid gap-8 lg:grid-cols-1">
                <article
                    class="p-6 bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700"
                    v-for="blog in response.data.results">
                    <BlogCard :blog="blog" />
                </article>
            </div>
        </div>
        <footer>
            <Pagination :data="data_pagination" />
        </footer>
    </section>
</template>

<script setup>
const cookie = useCookie('sessionid')  // Написать пагинацию, активные ссылки готовы

const response = await $fetch(`/api/blogs/getBlog`, {
    method: "post",
    body: {
        cookie: cookie.value
    }
})

if (response.auth === false) {
    navigateTo('/auth/')
} if (response.error) {
    throw createError()  // Написать страницу ошибок
}

const data_pagination = response.data

</script>
