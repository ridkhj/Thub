async function loadProducts() {
  const tbody = document.querySelector("tbody");
  const spinner = document.getElementById("spinner");
  const errorMsg = document.getElementById("errorMsg");

  tbody.innerHTML = "";
  spinner.style.display = "block";
  errorMsg.style.display = "none";

  try {
    const res = await fetch("http://localhost:5000/produtos");

    if (!res.ok) {
      throw new Error(`Erro HTTP: ${res.status}`);
    }

    const products = await res.json();

    if (products.length === 0) {
      tbody.innerHTML = '<tr><td colspan="6">Nenhum produto encontrado.</td></tr>';
    } else {
      products.forEach((item) => {
        const line = document.createElement("tr");

        line.innerHTML = `
          <td>${item.nome}</td>
          <td>${item.quantidade}</td>
          <td>${item.preco}</td>
          <td>${item.marca}</td>
          <td>${item.fornecedor_id}</td>
          <td>
            <div class="buttons">
              <button onclick="openEditModal('${item._id.$oid}')" class="edit"><i class="ph ph-pencil"></i> Editar</button>
              <button onclick="deletProduct('${item._id.$oid}')" class="remove"><i class="ph ph-trash"></i> Remover</button>
            </div>
          </td>
        `;

        tbody.appendChild(line);
      });
    }
  } catch (error) {
    console.error("Erro ao carregar produtos:", error);
    errorMsg.style.display = "block";
    tbody.innerHTML = '<tr><td colspan="6">Erro ao carregar produtos.</td></tr>';
  } finally {
    spinner.style.display = "none";
  }
}

async function deletProduct(id) {
  const confirmDelete = confirm("Tem certeza que deseja excluir este produto?");

  if (!confirmDelete) {
    return;
  }

  const res = await fetch(`http://localhost:5000/produtos/${id}`, {
    method: "DELETE",
  });

  if (!res.ok) {
    throw new Error(`Erro HTTP: ${res.status}`);
  }

  loadProducts();
}

async function openEditModal(id) {
  const res = await fetch("http://localhost:5000/produtos");

  if (!res.ok) {
    throw new Error(`Erro HTTP: ${res.status}`);
  }

  const products = await res.json();
  const product = products.find((p) => p._id.$oid === id);
  
  document.getElementById("editId").value = id;
  document.getElementById("editNome").value = product.nome;
  document.getElementById("editQuantidade").value = product.quantidade;
  document.getElementById("editPreco").value = product.preco;
  document.getElementById("editMarca").value = product.marca;
  document.getElementById("editFornecedor_id").value = product.fornecedor_id;

  document.getElementById("editProductModal").style.display = "flex";
}

function closeEditModal() {
  document.getElementById("editProductModal").style.display = "none";
}

document.getElementById("editProductForm").addEventListener("submit", async (event) => {
  event.preventDefault();

  const id = document.getElementById("editId").value;
  const updatedProduct = {
    nome: document.getElementById("editNome").value,
    quantidade: document.getElementById("editQuantidade").value,
    preco: document.getElementById("editPreco").value,
    marca: document.getElementById("editMarca").value,
    fornecedor_id: document.getElementById("editFornecedor_id").value,
  };

  try {
    const res = await fetch(`http://localhost:5000/produtos/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(updatedProduct),
    });

    if (!res.ok) {
      throw new Error(`Erro HTTP: ${res.status}`);
    }

    closeEditModal();
    loadProducts(); // Atualiza a lista de produtos
  } catch (error) {
    console.error("Erro ao editar produto:", error);
  }
});

function openAddModal() {
    document.getElementById("addProductModal").style.display = "flex";
}

function closeAddModal() {
    document.getElementById("addProductModal").style.display = "none";
}

document.getElementById("addProductForm").addEventListener("submit", async (event) => {
  event.preventDefault();

  const newProduct = {
    nome: document.getElementById("addNome").value,
    quantidade: Number(document.getElementById("addQuantidade").value),
    preco: Number(document.getElementById("addPreco").value),
    marca: document.getElementById("addMarca").value,
    fornecedor_id: document.getElementById("addFornecedor_id").value,
    categoria: "Pneus"
  };

  try {
    const res = await fetch("http://localhost:5000/produtos", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newProduct),
    });

    if (!res.ok) {
        throw new Error(`Erro HTTP: ${res.status}`);
    }

    closeAddModal();
    loadProducts();
  } catch (error) {
    console.error("Erro ao adicionar produto:", error);
  }
});

window.addEventListener("DOMContentLoaded", loadProducts);
