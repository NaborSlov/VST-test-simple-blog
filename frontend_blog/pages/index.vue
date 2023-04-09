<template>
    <section class="bg-white dark:bg-gray-900">
        <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
            <div class="mx-auto max-w-screen-sm text-center lg:mb-16 mb-8">
                <h2 class="mb-4 text-3xl lg:text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Our Blog
                </h2>
                <p class="font-light text-gray-500 sm:text-xl dark:text-gray-400">We use an agile approach to test
                    assumptions and connect with the needs of your audience early and often.</p>
            </div>
            <div class="grid gap-8 lg:grid-cols-2">
                <article
                    class="p-6 bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700"
                    v-for="blog in blogs_one">
                    <BlogCard :blog="blog" />
                </article>
                <article
                    class="p-6 bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700"
                    v-for="blog in blogs_two">
                    <BlogCard :blog="blog" />
                </article>
            </div>
        </div>
        <footer>
            <Pagination />
        </footer>
    </section>
</template>

<script setup>
const cookie = useCookie('sessionid')

const response = await $fetch(`/api/getBlog`, {
    method: "post",
    body: {
        cookie: cookie.value
    }
})

if (response.auth === false) {
    navigateTo('/auth/')
} if (response.error) {
    createError()  // Написать страницу ошибок
}

const length_results = response.data.results.length / 2
const blogs_one = response.data.results.slice(0, length_results)
const blogs_two = response.data.results.slice(-length_results)

</script>
