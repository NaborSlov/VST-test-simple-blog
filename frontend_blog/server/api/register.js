import axios from "axios"

export default defineEventHandler(async (event) => {
    const data = await readBody(event)
    const { webHost } = useRuntimeConfig()
    const url = `${webHost}/reg/`

    try {
        const response = await axios({
            method: 'post',
            url: url,
            data: {
                username: data.username,
                password: data.password,
                confirm_password: data.confirm_password,
            }
        })

        const cookies = response.headers['set-cookie']
        cookies.forEach(cookie => {
            const [key, value] = cookie.split(';')[0].split('=')
            setCookie(event, key, value)
        })

        return { data: response.data }

    }
    catch (error) {
        if (error.response !== undefined) {
            if (error.response.status === 400) {
                return { bad: true }
            }
        }

        return { error: error.message }
    }
})