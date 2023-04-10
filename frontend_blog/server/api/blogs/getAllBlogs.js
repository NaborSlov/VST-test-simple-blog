import axios from "axios"


export default defineEventHandler(async (event) => {
    const formData = await readBody(event)
    const { webHost } = useRuntimeConfig()

    let url = `${webHost}/api/blogs/`

    if (formData.offset) {
        url += `?limit=10&offset=${formData.offset}`
    }


    try {
        const { data } = await axios({
            method: "get",
            url: url,
            headers: {
                "cookie": `sessionid=${formData.cookie}`
            }
        })

        return { data: data, auth: true }
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

