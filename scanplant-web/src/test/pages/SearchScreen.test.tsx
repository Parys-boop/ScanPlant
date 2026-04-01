import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { vi } from 'vitest';
import userEvent from '@testing-library/user-event';
import SearchScreen from '../../pages/SearchScreen';
import { database } from '../../api';

vi.mock('../../api', () => ({
  database: {
    select: vi.fn(),
  },
}));

describe('SearchScreen', () => {
  afterEach(() => {
    vi.clearAllMocks();
  });

  it('loads plants from the API and renders the list', async () => {
    vi.mocked(database.select).mockResolvedValue({
      data: [
        {
          id: 'plant-1',
          common_name: 'Samambaia',
          scientific_name: 'Nephrolepis exaltata',
          image_data: '',
          city: 'Curitiba',
          created_at: '2026-03-29T10:00:00.000Z',
        },
        {
          id: 'plant-2',
          common_name: 'Orquidea',
          scientific_name: 'Orchidaceae',
          image_data: '',
          city: 'Sao Paulo',
          created_at: '2026-03-30T10:00:00.000Z',
        },
      ],
      error: null,
    });

    render(
      <MemoryRouter>
        <SearchScreen />
      </MemoryRouter>,
    );

    expect(screen.getByText('Explorar Plantas')).toBeInTheDocument();
    expect(await screen.findByText('Orquidea')).toBeInTheDocument();
    expect(screen.getByText('Samambaia')).toBeInTheDocument();
    expect(database.select).toHaveBeenCalledWith('plants');
  });

  it('filters plants using the selected search type', async () => {
    const user = userEvent.setup();

    vi.mocked(database.select).mockResolvedValue({
      data: [
        {
          id: 'plant-1',
          common_name: 'Rosa',
          scientific_name: 'Rosa rubiginosa',
          image_data: '',
          city: 'Sao Paulo',
          created_at: '2026-03-30T10:00:00.000Z',
        },
        {
          id: 'plant-2',
          common_name: 'Lirio',
          scientific_name: 'Lilium candidum',
          image_data: '',
          city: 'Curitiba',
          created_at: '2026-03-29T10:00:00.000Z',
        },
      ],
      error: null,
    });

    render(
      <MemoryRouter>
        <SearchScreen />
      </MemoryRouter>,
    );

    const searchInput = await screen.findByPlaceholderText('Digite sua busca...');
    await user.type(searchInput, 'sao');

    expect(await screen.findByText('Nenhuma planta encontrada')).toBeInTheDocument();

    await user.selectOptions(screen.getByRole('combobox'), 'city');

    expect(await screen.findByText('Rosa')).toBeInTheDocument();
    expect(screen.queryByText('Nenhuma planta encontrada')).not.toBeInTheDocument();
  });

  it('shows the empty state when the API returns no plants', async () => {
    vi.mocked(database.select).mockResolvedValue({
      data: [],
      error: null,
    });

    render(
      <MemoryRouter>
        <SearchScreen />
      </MemoryRouter>,
    );

    expect(await screen.findByText('Nenhuma planta encontrada')).toBeInTheDocument();
  });
});
