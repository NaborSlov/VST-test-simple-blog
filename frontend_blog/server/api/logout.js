import axios from "axios"

export default defineEventHandler(async (event) => {
    const cookie = getCookie(event, 'sessionid')
    const { webHost } = useRuntimeConfig()

    const url = `${webHost}/logout/`

    try {
        const response = await axios({
            method: 'get',
            url: url,
            headers: {
                "cookie": `sessionid=${cookie}`
            }
        })

        return { data: response.data }
    }
    catch (error) {
        return { error: error.message }
    }


    
})