export default async function handler(req, res) {
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    const { eventName, eventSourceUrl } = req.body;
    const pixelId = '1352856539261316';
    const accessToken = 'EAA1SWfhZC7l4BQLP2EYZC4MbEMyOWMBQZBIaCYv6tqWZAhlSVBsZCBDOOdfayCPvy0Bq3RFrz6pj4OFmGKW7mcU5WQyaAVWWs6OkepxNM6HxVo3E4YT9LrGTM9yZB9u9kbbjzwGoOwQYkBdJo2WHjCoB4btYJ04TXFWVoYQLnZAOqwxYe3ujDTGPmOifZBYx3AZDZD';

    try {
        const response = await fetch(`https://graph.facebook.com/v19.0/${pixelId}/events?access_token=${accessToken}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                data: [
                    {
                        event_name: eventName,
                        event_time: Math.floor(Date.now() / 1000),
                        event_source_url: eventSourceUrl,
                        action_source: 'website',
                        user_data: {
                            client_user_agent: req.headers['user-agent'],
                            client_ip_address: req.headers['x-forwarded-for'] || req.socket.remoteAddress
                        }
                    },
                ],
            }),
        });

        const data = await response.json();
        console.log('FB CAPI Response:', data);
        return res.status(200).json(data);
    } catch (error) {
        console.error('Facebook CAPI Error:', error);
        return res.status(500).json({ error: 'Internal Server Error' });
    }
}
