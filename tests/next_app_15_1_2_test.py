import pytest

from techs.next_app_15 import NextApp1512


@pytest.fixture
def app():
    return NextApp1512()


def test_get_documentation_links(app: NextApp1512):
    links = set(app.docs_urls())
    assert links == {
        "https://nextjs.org/docs/app/api-reference/cli",
        "https://nextjs.org/docs/app/api-reference/cli/create-next-app",
        "https://nextjs.org/docs/app/api-reference/cli/next",
        "https://nextjs.org/docs/app/api-reference/components",
        "https://nextjs.org/docs/app/api-reference/components/font",
        "https://nextjs.org/docs/app/api-reference/components/form",
        "https://nextjs.org/docs/app/api-reference/components/image",
        "https://nextjs.org/docs/app/api-reference/components/link",
        "https://nextjs.org/docs/app/api-reference/components/script",
        "https://nextjs.org/docs/app/api-reference/config",
        "https://nextjs.org/docs/app/api-reference/config/eslint",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/appDir",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/compress",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/dynamicIO",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/env",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/eslint",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/headers",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/images",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/logging",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/output",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/ppr",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactStrictMode",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/turbo",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/useLightningcss",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/webVitalsAttribution",
        "https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack",
        "https://nextjs.org/docs/app/api-reference/config/typescript",
        "https://nextjs.org/docs/app/api-reference/directives",
        "https://nextjs.org/docs/app/api-reference/directives/use-cache",
        "https://nextjs.org/docs/app/api-reference/directives/use-client",
        "https://nextjs.org/docs/app/api-reference/directives/use-server",
        "https://nextjs.org/docs/app/api-reference/edge",
        "https://nextjs.org/docs/app/api-reference/file-conventions",
        "https://nextjs.org/docs/app/api-reference/file-conventions/default",
        "https://nextjs.org/docs/app/api-reference/file-conventions/error",
        "https://nextjs.org/docs/app/api-reference/file-conventions/forbidden",
        "https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation",
        "https://nextjs.org/docs/app/api-reference/file-conventions/layout",
        "https://nextjs.org/docs/app/api-reference/file-conventions/loading",
        "https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components",
        "https://nextjs.org/docs/app/api-reference/file-conventions/metadata",
        "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons",
        "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest",
        "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image",
        "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots",
        "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap",
        "https://nextjs.org/docs/app/api-reference/file-conventions/middleware",
        "https://nextjs.org/docs/app/api-reference/file-conventions/not-found",
        "https://nextjs.org/docs/app/api-reference/file-conventions/page",
        "https://nextjs.org/docs/app/api-reference/file-conventions/route",
        "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config",
        "https://nextjs.org/docs/app/api-reference/file-conventions/template",
        "https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized",
        "https://nextjs.org/docs/app/api-reference/functions",
        "https://nextjs.org/docs/app/api-reference/functions/after",
        "https://nextjs.org/docs/app/api-reference/functions/cacheLife",
        "https://nextjs.org/docs/app/api-reference/functions/cacheTag",
        "https://nextjs.org/docs/app/api-reference/functions/connection",
        "https://nextjs.org/docs/app/api-reference/functions/cookies",
        "https://nextjs.org/docs/app/api-reference/functions/draft-mode",
        "https://nextjs.org/docs/app/api-reference/functions/fetch",
        "https://nextjs.org/docs/app/api-reference/functions/forbidden",
        "https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata",
        "https://nextjs.org/docs/app/api-reference/functions/generate-metadata",
        "https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps",
        "https://nextjs.org/docs/app/api-reference/functions/generate-static-params",
        "https://nextjs.org/docs/app/api-reference/functions/generate-viewport",
        "https://nextjs.org/docs/app/api-reference/functions/headers",
        "https://nextjs.org/docs/app/api-reference/functions/image-response",
        "https://nextjs.org/docs/app/api-reference/functions/next-request",
        "https://nextjs.org/docs/app/api-reference/functions/next-response",
        "https://nextjs.org/docs/app/api-reference/functions/not-found",
        "https://nextjs.org/docs/app/api-reference/functions/permanentRedirect",
        "https://nextjs.org/docs/app/api-reference/functions/redirect",
        "https://nextjs.org/docs/app/api-reference/functions/revalidatePath",
        "https://nextjs.org/docs/app/api-reference/functions/revalidateTag",
        "https://nextjs.org/docs/app/api-reference/functions/unauthorized",
        "https://nextjs.org/docs/app/api-reference/functions/unstable_cache",
        "https://nextjs.org/docs/app/api-reference/functions/unstable_expirePath",
        "https://nextjs.org/docs/app/api-reference/functions/unstable_expireTag",
        "https://nextjs.org/docs/app/api-reference/functions/unstable_noStore",
        "https://nextjs.org/docs/app/api-reference/functions/unstable_rethrow",
        "https://nextjs.org/docs/app/api-reference/functions/use-params",
        "https://nextjs.org/docs/app/api-reference/functions/use-pathname",
        "https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals",
        "https://nextjs.org/docs/app/api-reference/functions/use-router",
        "https://nextjs.org/docs/app/api-reference/functions/use-search-params",
        "https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment",
        "https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments",
        "https://nextjs.org/docs/app/api-reference/functions/userAgent",
        "https://nextjs.org/docs/app/api-reference/turbopack",
        "https://nextjs.org/docs/app/building-your-application/authentication",
        "https://nextjs.org/docs/app/building-your-application/caching",
        "https://nextjs.org/docs/app/building-your-application/configuring",
        "https://nextjs.org/docs/app/building-your-application/configuring/content-security-policy",
        "https://nextjs.org/docs/app/building-your-application/configuring/custom-server",
        "https://nextjs.org/docs/app/building-your-application/configuring/debugging",
        "https://nextjs.org/docs/app/building-your-application/configuring/draft-mode",
        "https://nextjs.org/docs/app/building-your-application/configuring/environment-variables",
        "https://nextjs.org/docs/app/building-your-application/configuring/mdx",
        "https://nextjs.org/docs/app/building-your-application/configuring/progressive-web-apps",
        "https://nextjs.org/docs/app/building-your-application/configuring/src-directory",
        "https://nextjs.org/docs/app/building-your-application/data-fetching",
        "https://nextjs.org/docs/app/building-your-application/data-fetching/fetching",
        "https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration",
        "https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations",
        "https://nextjs.org/docs/app/building-your-application/deploying",
        "https://nextjs.org/docs/app/building-your-application/deploying/multi-zones",
        "https://nextjs.org/docs/app/building-your-application/deploying/production-checklist",
        "https://nextjs.org/docs/app/building-your-application/deploying/static-exports",
        "https://nextjs.org/docs/app/building-your-application/optimizing",
        "https://nextjs.org/docs/app/building-your-application/optimizing/analytics",
        "https://nextjs.org/docs/app/building-your-application/optimizing/fonts",
        "https://nextjs.org/docs/app/building-your-application/optimizing/images",
        "https://nextjs.org/docs/app/building-your-application/optimizing/instrumentation",
        "https://nextjs.org/docs/app/building-your-application/optimizing/lazy-loading",
        "https://nextjs.org/docs/app/building-your-application/optimizing/memory-usage",
        "https://nextjs.org/docs/app/building-your-application/optimizing/metadata",
        "https://nextjs.org/docs/app/building-your-application/optimizing/open-telemetry",
        "https://nextjs.org/docs/app/building-your-application/optimizing/package-bundling",
        "https://nextjs.org/docs/app/building-your-application/optimizing/scripts",
        "https://nextjs.org/docs/app/building-your-application/optimizing/static-assets",
        "https://nextjs.org/docs/app/building-your-application/optimizing/third-party-libraries",
        "https://nextjs.org/docs/app/building-your-application/optimizing/videos",
        "https://nextjs.org/docs/app/building-your-application/rendering",
        "https://nextjs.org/docs/app/building-your-application/rendering/client-components",
        "https://nextjs.org/docs/app/building-your-application/rendering/composition-patterns",
        "https://nextjs.org/docs/app/building-your-application/rendering/edge-and-nodejs-runtimes",
        "https://nextjs.org/docs/app/building-your-application/rendering/partial-prerendering",
        "https://nextjs.org/docs/app/building-your-application/rendering/server-components",
        "https://nextjs.org/docs/app/building-your-application/routing",
        "https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes",
        "https://nextjs.org/docs/app/building-your-application/routing/error-handling",
        "https://nextjs.org/docs/app/building-your-application/routing/intercepting-routes",
        "https://nextjs.org/docs/app/building-your-application/routing/internationalization",
        "https://nextjs.org/docs/app/building-your-application/routing/layouts-and-templates",
        "https://nextjs.org/docs/app/building-your-application/routing/linking-and-navigating",
        "https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming",
        "https://nextjs.org/docs/app/building-your-application/routing/middleware",
        "https://nextjs.org/docs/app/building-your-application/routing/parallel-routes",
        "https://nextjs.org/docs/app/building-your-application/routing/redirecting",
        "https://nextjs.org/docs/app/building-your-application/routing/route-groups",
        "https://nextjs.org/docs/app/building-your-application/routing/route-handlers",
        "https://nextjs.org/docs/app/building-your-application/styling",
        "https://nextjs.org/docs/app/building-your-application/styling/css",
        "https://nextjs.org/docs/app/building-your-application/styling/css-in-js",
        "https://nextjs.org/docs/app/building-your-application/styling/sass",
        "https://nextjs.org/docs/app/building-your-application/styling/tailwind-css",
        "https://nextjs.org/docs/app/building-your-application/testing",
        "https://nextjs.org/docs/app/building-your-application/testing/cypress",
        "https://nextjs.org/docs/app/building-your-application/testing/jest",
        "https://nextjs.org/docs/app/building-your-application/testing/playwright",
        "https://nextjs.org/docs/app/building-your-application/testing/vitest",
        "https://nextjs.org/docs/app/building-your-application/upgrading",
        "https://nextjs.org/docs/app/building-your-application/upgrading/app-router-migration",
        "https://nextjs.org/docs/app/building-your-application/upgrading/canary",
        "https://nextjs.org/docs/app/building-your-application/upgrading/codemods",
        "https://nextjs.org/docs/app/building-your-application/upgrading/from-create-react-app",
        "https://nextjs.org/docs/app/building-your-application/upgrading/from-vite",
        "https://nextjs.org/docs/app/building-your-application/upgrading/version-14",
        "https://nextjs.org/docs/app/building-your-application/upgrading/version-15",
        "https://nextjs.org/docs/app/getting-started",
        "https://nextjs.org/docs/app/getting-started/css-and-styling",
        "https://nextjs.org/docs/app/getting-started/data-fetching-and-streaming",
        "https://nextjs.org/docs/app/getting-started/images-and-fonts",
        "https://nextjs.org/docs/app/getting-started/installation",
        "https://nextjs.org/docs/app/getting-started/layouts-and-pages",
        "https://nextjs.org/docs/app/getting-started/project-structure",
    }


def test_llms_txt(app: NextApp1512):
    page = app.llms_txt("https://nextjs.org/docs/app/getting-started/layouts-and-pages")

    assert page.id == "nextjs_app_router"
    assert page.name == "NextJS"
    assert page.version == "15.1.2"
    assert page.url == "https://nextjs.org/docs/app/getting-started/layouts-and-pages"
    assert (
        page.content
        == """
# How to create layouts and pages

Next.js uses **file-system based routing**, meaning you can use folders and files to define routes. This page will guide you through how to create layouts and pages, and link between them.

## Creating a page

A **page** is UI that is rendered on a specific route. To create a page, add a `page` file inside the `app` directory and default export a React component. For example, to create an index page (`/`):


app/page.tsx
```
export default function Page() {
  return <h1>Hello Next.js!</h1>
}
```

## Creating a layout

A layout is UI that is **shared** between multiple pages. On navigation, layouts preserve state, remain interactive, and do not rerender.

You can define a layout by default exporting a React component from a `layout` file. The component should accept a `children` prop which can be a page or another layout.

For example, to create a layout that accepts your index page as child, add a `layout` file inside the `app` directory:


app/layout.tsx
```
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        {/* Layout UI */}
        {/* Place children where you want to render a page or nested layout */}
        <main>{children}</main>
      </body>
    </html>
  )
}
```

The layout above is called a root layout because it\'s defined at the root of the `app` directory. The root layout is **required** and must contain `html` and `body` tags.

## Creating a nested route

A nested route is a route composed of multiple URL segments. For example, the `/blog/[slug]` route is composed of three segments:

* `/` (Root Segment)
* `blog` (Segment)
* `[slug]` (Leaf Segment)

In Next.js:

* **Folders** are used to define the route segments that map to URL segments.
* **Files** (like `page` and `layout`) are used to create UI that is shown for a segment.

To create nested routes, you can nest folders inside each other. For example, to add a route for `/blog`, create a folder called `blog` in the `app` directory. Then, to make `/blog` publicly accessible, add a `page` file:


app/blog/page.tsx
```
import { getPosts } from \'@/lib/posts\'
import { Post } from \'@/ui/post\'

export default async function Page() {
  const posts = await getPosts()

  return (
    <ul>
      {posts.map((post) => (
        <Post key={post.id} post={post} />
      ))}
    </ul>
  )
}
```

You can continue nesting folders to create nested routes. For example, to create a route for a specific blog post, create a new `[slug]` folder inside `blog` and add a `page` file:


app/blog/[slug]/page.tsx
```
function generateStaticParams() {}

export default function Page() {
  return <h1>Hello, Blog Post Page!</h1>
}
```

> **Good to know**: Wrapping a folder name in square brackets (e.g. `[slug]`) creates a special dynamic route segment used to generate multiple pages from data. This is useful for blog posts, product pages, etc.

## Nesting layouts

By default, layouts in the folder hierarchy are also nested, which means they wrap child layouts via their `children` prop. You can nest layouts by adding `layout` inside specific route segments (folders).

For example, to create a layout for the `/blog` route, add a new `layout` file inside the `blog` folder.


app/blog/layout.tsx
```
export default function BlogLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return <section>{children}</section>
}
```

If you were to combine the two layouts above, the root layout (`app/layout.js`) would wrap the blog layout (`app/blog/layout.js`), which would wrap the blog (`app/blog/page.js`) and blog post page (`app/blog/[slug]/page.js`).

## Linking between pages

You can use the `<Link>` component to navigate between routes. `<Link>` is a built-in Next.js component that extends the HTML `<a>` tag to provide prefetching and client-side navigation.

For example, to generate a list of blog posts, import `<Link>` from `next/link` and pass a `href` prop to the component:

app/ui/post.tsx
```
import Link from \'next/link\'

export default async function Post({ post }) {
  const posts = await getPosts()

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.slug}>
          <Link href={`/blog/${post.slug}`}>{post.title}</Link>
        </li>
      ))}
    </ul>
  )
}
```

`<Link>` is the primary and recommended way to navigate between routes in your Next.js application. However, you can also use the `useRouter` hook for more advanced navigation.
    """.strip()
    )


def test_page_chunks(app: NextApp1512):
    docs = app.page_chunks("https://nextjs.org/docs/app/getting-started/layouts-and-pages")
    assert docs[0].id == "nextjs_app_router"
    assert docs[0].name == "NextJS"
    assert docs[0].version == "15.1.2"
    assert docs[0].url == "https://nextjs.org/docs/app/getting-started/layouts-and-pages"
    assert docs[0].content.startswith(
        "[[ ## NextJS 15.1.2 app router documentation ]]\n\n# How to create layouts and pages"
    )
