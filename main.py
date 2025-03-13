from fastapi import FastAPI, Query
import guessit

app = FastAPI()

@app.get("/parse")
async def read_root(filename=Query(None)):
    info = guessit.guessit(filename)
    # 'Shogun.S01E01.2024.2160p.DSNP.WEB-DL.DDP5.1.DV.HDR.H.265-HHWEB.mkv'
    return {
        'title': info.get('title'),
        'year': info.get('year'),
        'type': 'movie' if info.get('type') == 'movie' else 'tv',
        'season': info.get('season'),
        'episode': info.get('episode')
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=7788)