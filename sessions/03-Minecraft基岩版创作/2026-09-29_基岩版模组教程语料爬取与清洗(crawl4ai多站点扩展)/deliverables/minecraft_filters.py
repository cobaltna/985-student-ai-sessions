"""
Minecraft 文档专用 URL 过滤器和评分器（按站点参数化）
"""

from fnmatch import fnmatch

from crawl4ai.deep_crawling.filters import (
    FilterChain,
    URLPatternFilter,
    DomainFilter,
)
from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer

from config.crawler_config import SiteConfig


def _fnmatch_any(url: str, patterns) -> bool:
    return any(fnmatch(url, p) for p in patterns)


def create_filter_chain(site: SiteConfig) -> FilterChain:
    """按站点配置构建过滤链：域名白名单 + URL 模式白名单 + 黑名单"""

    filters = [
        DomainFilter(
            allowed_domains=site.allowed_domains,
            blocked_domains=[]
        ),
    ]

    if site.allowed_patterns:
        filters.append(URLPatternFilter(patterns=site.allowed_patterns))

    if site.blocked_patterns:
        filters.append(URLPatternFilter(
            patterns=site.blocked_patterns,
            reverse=True,  # 命中黑名单即排除
        ))

    return FilterChain(filters)


def create_scorer(site: SiteConfig) -> KeywordRelevanceScorer:
    """按站点关键词创建 URL 评分器，优先抓取高价值页面"""
    return KeywordRelevanceScorer(
        keywords=site.keywords or ["minecraft"],
        weight=1.0
    )


def url_allowed(site: SiteConfig, url: str) -> bool:
    """url_list 模式下的最终 URL 核验（与深度爬取过滤规则一致）"""
    from urllib.parse import urlparse

    host = urlparse(url).netloc
    if host not in site.allowed_domains:
        return False
    if site.allowed_patterns and not _fnmatch_any(url, site.allowed_patterns):
        return False
    if site.blocked_patterns and _fnmatch_any(url, site.blocked_patterns):
        return False
    return True
