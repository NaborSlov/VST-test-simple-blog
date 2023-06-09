import axios from "axios";

export default defineEventHandler(async (event) => {
    const { username, password } = await readBody(event)
    const { webHost } = useRuntimeConfig()

    try {
        const response = await axios({
            method: "post",
            url: `${webHost}/login/`,
            data: {
                username: username,
                password: password
            }
        })

        const cookies = response.headers['set-cookie']
        cookies.forEach(cookie => {
            const [key, value] = cookie.split(';')[0].split('=')
            setCookie(event, key, value)
        })

        return { data: response.data, auth: true }
    }
    catch (error) {
        if (error.response !== undefined) {
            if (error.response.status === 403) {
                return { auth: false }
            }
        }

        return { error: error.message }
    }
})
