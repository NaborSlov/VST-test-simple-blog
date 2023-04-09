import axios from "axios"

export default defineEventHandler(async (event) => {
    const cookie = getCookie(event, 'sessionid')
    const { webHost } = useRuntimeConfig()

    const url = `${webHost}/logout/`

    const response = await axios({
        method: 'get',
        url: url,
        headers: {
            "cookie": `sessionid=${cookie}`
        }
    })
})