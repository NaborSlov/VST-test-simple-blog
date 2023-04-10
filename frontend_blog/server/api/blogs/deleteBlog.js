import axios from "axios"


export default defineEventHandler(async (event) => {
    const formData = await readBody(event)
    const { webHost } = useRuntimeConfig()

    let url = `${webHost}/api/blogs/update/${formData.id}/`

    try {
        const response = await axios({
            method: "delete",
            url: url,
            headers: {
                "cookie": `sessionid=${formData.cookie};csrftoken=${formData.csrf_token}`,
                "x-csrftoken": formData.csrf_token,
            },
        })

        return { response: response.data }

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
