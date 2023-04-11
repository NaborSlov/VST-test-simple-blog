import axios from "axios"

export default defineEventHandler(async (event) => {
    const formData = await readBody(event)
    const { webHost } = useRuntimeConfig()

    const url = `${webHost}/logout/`

    try {
        const response = await axios({
            method: 'delete',
            url: url,
            headers: {
                "cookie": `sessionid=${formData.cookie};csrftoken=${formData.csrf_token}`,
                "x-csrftoken": formData.csrf_token,
            }
        })

        return { data: response.data }
    }
    catch (error) {
        return { error: error.message }
    }


    
})