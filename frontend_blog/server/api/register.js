export default defineEventHandler(async (event) => {
    const data = await readBody()
    const { webHost } = useRuntimeConfig()

    await $fetch(`${webHost}/reg`, {
        method: 'post',
        body: {
            username: data.username,
            password: data.password,
            confirm_password: data.confirm_password,
        }
    })
})