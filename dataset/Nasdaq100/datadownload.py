# python /container/volume_data/Time-LLM/dataset/Nasdaq100/datadownload.py
import yfinance as yf
import pandas as pd

def download_nasdaq100(start_date: str, end_date: str, filename: str = None):
    """
    NASDAQ-100 (^NDX) 지수 데이터를 다운로드하고
    Open, High, Low, Close, Volume 컬럼만 남긴 뒤 반환합니다.
    optionally CSV 파일로 저장할 수도 있습니다.
    
    :param start_date: 조회 시작일자, 예: '2019-01-01'
    :param end_date: 조회 종료일자, 예: '2023-12-31'
    :param filename: CSV로 저장할 파일명 (None이면 저장하지 않음)
    :return: pandas.DataFrame
    """
    # ^NDX: NASDAQ-100 지수
    ticker = "^NDX"
    
    # 데이터 다운로드
    df = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        interval="1d",
        auto_adjust=False,    # true로 하면 주가조정(close 등)이 적용됨
        progress=True
    )
    print(df.columns)
    # 필요한 컬럼만 선택
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    
    # 인덱스를 날짜형으로 변환 (이미 DatetimeIndex이지만, 안전 차원)
    df.index = pd.to_datetime(df.index)
    
    # CSV로 저장 (필요 시)
    if filename:
        df.to_csv(filename, encoding="utf-8-sig")
        print(f"Saved data to {filename}")
    
    return df

if __name__ == "__main__":
    # 다운로드 기간 설정
    start = "1995-01-01"
    end   = "2024-12-31"
    
    filename = "/container/volume_data/Time-LLM/dataset/Nasdaq100/nasdaq100.csv"
    # 데이터 가져오기 (CSV로도 저장)
    data = download_nasdaq100(start, end, filename=filename)
    
    # 상위 5개 행 출력
    print(data.head())
