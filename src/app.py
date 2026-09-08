from datetime import datetime, timezone
import math, statistics

def validate_prices(rows):
    issues=[]
    for i,row in enumerate(rows):
        if row["close"] <= 0: issues.append({"row":i,"issue":"non_positive_price"})
        if row["high"] < max(row["open"],row["close"]) or row["low"] > min(row["open"],row["close"]): issues.append({"row":i,"issue":"invalid_ohlc"})
    return issues
def log_returns(closes): return [math.log(b/a) for a,b in zip(closes,closes[1:])]
def historical_var(closes, confidence=.95):
    returns=sorted(log_returns(closes)); index=max(0,int((1-confidence)*len(returns))-1)
    return round(-returns[index],6)
def run_manifest(rows):
    closes=[r["close"] for r in rows]
    return {"run_at":datetime.now(timezone.utc).isoformat(),"rows":len(rows),"quality_issues":validate_prices(rows),"mean_return":round(statistics.mean(log_returns(closes)),6),"var_95":historical_var(closes)}

if __name__ == "__main__":
    rows=[{"open":100,"high":103,"low":99,"close":102},{"open":102,"high":104,"low":101,"close":103},{"open":103,"high":103,"low":98,"close":99}]
    print(run_manifest(rows))
